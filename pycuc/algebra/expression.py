from __future__ import annotations

import ast
from fractions import Fraction
from typing import Literal, Mapping, Protocol, runtime_checkable

from .base import expand_to_base_units
from .compatibility import require_compatible
from .derived import reduce_derived_unit
from .parser import parse_unit
from .unit import UnitExpr, to_fraction


@runtime_checkable
class HasUnit(Protocol):
    """Structural protocol for objects exposing a unit attribute."""

    unit: str | None


UnitSource = UnitExpr | str | None | HasUnit
UnitStyle = Literal["derived", "base", "raw"]


_DIMENSIONLESS_UNARY_FUNCTIONS = {
    "exp",
    "log",
    "ln",
    "log10",
    "sin",
    "cos",
    "tan",
    "asin",
    "acos",
    "atan",
    "sinh",
    "cosh",
    "tanh",
    "asinh",
    "acosh",
    "atanh",
}


_UNIT_PRESERVING_UNARY_FUNCTIONS = {
    "abs",
    "fabs",
}


def infer_unit(
    expression: str,
    units: Mapping[str, UnitSource],
) -> UnitExpr:
    """
    Infer the symbolic result unit of a mathematical expression.

    This function performs algebraic cancellation only. Use
    :func:`infer_unit_string` to choose the final representation style.
    """
    tree = ast.parse(expression, mode="eval")
    return _infer_node(tree.body, units)


def infer_unit_string(
    expression: str,
    units: Mapping[str, UnitSource],
    *,
    unit_style: UnitStyle = "derived",
    derived: bool | None = None,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Infer and format the result unit using the requested representation.

    Parameters
    ----------
    unit_style : {"derived", "base", "raw"}, default="derived"
        ``"derived"`` reduces recognizable composites to preferred SI-derived
        symbols, e.g. ``kg.m/s^2 -> N`` and ``J/m^3 -> Pa``.
        ``"base"`` expands supported derived symbols to SI base units, e.g.
        ``N -> kg.m/s^2`` and ``Pa -> kg/(m.s^2)``.
        ``"raw"`` performs symbolic cancellation only.
    derived : bool | None, optional
        Backward-compatible alias. ``True`` maps to ``unit_style="derived"``
        and ``False`` maps to ``unit_style="raw"``. Prefer ``unit_style`` for
        new code.
    """
    if derived is not None:
        unit_style = "derived" if derived else "raw"

    if unit_style not in {"derived", "base", "raw"}:
        raise ValueError(
            "unit_style must be one of 'derived', 'base', or 'raw'."
        )

    result = infer_unit(expression, units)

    if unit_style == "derived":
        result = reduce_derived_unit(result)
    elif unit_style == "base":
        result = expand_to_base_units(result)

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def _unit_from_source(source: UnitSource) -> UnitExpr:
    if isinstance(source, UnitExpr):
        return source

    if isinstance(source, str) or source is None:
        return parse_unit(source)

    if hasattr(source, "unit"):
        return parse_unit(source.unit)

    raise TypeError(
        "Unit sources must be UnitExpr, str, None, or an object with '.unit'."
    )


def _infer_node(
    node: ast.AST,
    units: Mapping[str, UnitSource],
) -> UnitExpr:
    if isinstance(node, ast.Name):
        if node.id not in units:
            raise KeyError(f"No unit supplied for variable {node.id!r}.")
        return _unit_from_source(units[node.id])

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return UnitExpr.dimensionless()
        raise TypeError("Only numeric constants are supported in expressions.")

    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        return _infer_node(node.operand, units)

    if isinstance(node, ast.BinOp):
        if isinstance(node.op, (ast.Add, ast.Sub)):
            left = _infer_node(node.left, units)
            right = _infer_node(node.right, units)
            return require_compatible(left, right, context="addition/subtraction")

        if isinstance(node.op, ast.Mult):
            return _infer_node(node.left, units) * _infer_node(node.right, units)

        if isinstance(node.op, ast.Div):
            return _infer_node(node.left, units) / _infer_node(node.right, units)

        if isinstance(node.op, ast.Pow):
            base = _infer_node(node.left, units)
            exponent = _numeric_exponent(node.right)
            return base ** exponent

        raise TypeError(f"Unsupported binary operator: {type(node.op).__name__}.")

    if isinstance(node, ast.Call):
        return _infer_function_call(node, units)

    raise TypeError(f"Unsupported expression node: {type(node).__name__}.")


def _infer_function_call(
    node: ast.Call,
    units: Mapping[str, UnitSource],
) -> UnitExpr:
    if not isinstance(node.func, ast.Name):
        raise TypeError("Only direct function calls such as exp(x) are supported.")

    function_name = node.func.id

    if node.keywords:
        raise TypeError("Keyword arguments are not supported in unit-aware calls.")

    if function_name == "sqrt":
        _require_arg_count(function_name, node.args, 1)
        return _infer_node(node.args[0], units) ** Fraction(1, 2)

    if function_name == "cbrt":
        _require_arg_count(function_name, node.args, 1)
        return _infer_node(node.args[0], units) ** Fraction(1, 3)

    if function_name in _UNIT_PRESERVING_UNARY_FUNCTIONS:
        _require_arg_count(function_name, node.args, 1)
        return _infer_node(node.args[0], units)

    if function_name in _DIMENSIONLESS_UNARY_FUNCTIONS:
        _require_arg_count(function_name, node.args, 1)
        argument_unit = _infer_node(node.args[0], units)
        _require_dimensionless(argument_unit, function_name)
        return UnitExpr.dimensionless()

    raise TypeError(
        f"Unsupported unit-aware function call: {function_name}(...)."
    )


def _require_arg_count(
    function_name: str,
    args: list[ast.expr],
    expected: int,
) -> None:
    if len(args) != expected:
        raise TypeError(
            f"{function_name}() expects {expected} argument(s), got {len(args)}."
        )


def _require_dimensionless(unit_expr: UnitExpr, function_name: str) -> None:
    if not unit_expr.is_dimensionless:
        raise ValueError(
            f"{function_name}() requires a dimensionless argument, "
            f"got {unit_expr.format()!r}."
        )


def _numeric_exponent(node: ast.AST) -> Fraction:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)) and not isinstance(node.value, bool):
            return to_fraction(node.value)

    if (
        isinstance(node, ast.UnaryOp)
        and isinstance(node.op, ast.USub)
        and isinstance(node.operand, ast.Constant)
        and isinstance(node.operand.value, (int, float))
        and not isinstance(node.operand.value, bool)
    ):
        return -to_fraction(node.operand.value)

    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        numerator = _numeric_exponent(node.left)
        denominator = _numeric_exponent(node.right)

        if denominator == 0:
            raise ValueError("Exponent denominator cannot be zero.")

        return numerator / denominator

    raise TypeError("Unit exponents must be numeric dimensionless constants.")
