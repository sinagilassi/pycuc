from __future__ import annotations

import ast
from fractions import Fraction
from typing import Mapping, Protocol, runtime_checkable

from .compatibility import require_compatible
from .parser import parse_unit
from .unit import UnitExpr, to_fraction


@runtime_checkable
class HasUnit(Protocol):
    """Structural protocol for objects exposing a unit attribute."""

    unit: str | None


UnitSource = UnitExpr | str | None | HasUnit


def infer_unit(
    expression: str,
    units: Mapping[str, UnitSource],
) -> UnitExpr:
    """
    Infer the result unit of a mathematical expression.

    Supported operators are +, -, *, /, **, unary +/- and sqrt(...).
    Addition/subtraction require compatible operand units.
    """
    tree = ast.parse(expression, mode="eval")
    return _infer_node(tree.body, units)


def infer_unit_string(
    expression: str,
    units: Mapping[str, UnitSource],
    *,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Infer and format the result unit of a mathematical expression."""
    return infer_unit(expression, units).format(
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
        if (
            isinstance(node.func, ast.Name)
            and node.func.id == "sqrt"
            and len(node.args) == 1
            and not node.keywords
        ):
            return _infer_node(node.args[0], units) ** Fraction(1, 2)

        raise TypeError("Only sqrt(x) is supported as a unit-aware function call.")

    raise TypeError(f"Unsupported expression node: {type(node).__name__}.")


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
