from __future__ import annotations

from typing import Literal

from .base import expand_to_base_units
from .derived import reduce_derived_unit
from .parser import parse_unit
from .unit import ExponentInput, UnitExpr


UnitStyle = Literal["derived", "base", "raw"]


def _apply_unit_style(
    value: UnitExpr,
    *,
    unit_style: UnitStyle,
    derived: bool | None,
) -> UnitExpr:
    if derived is not None:
        unit_style = "derived" if derived else "raw"

    if unit_style == "derived":
        return reduce_derived_unit(expand_to_base_units(value))
    if unit_style == "base":
        return expand_to_base_units(value)
    if unit_style == "raw":
        return value

    raise ValueError("unit_style must be one of 'derived', 'base', or 'raw'.")


def simplify_unit(
    value: UnitExpr | str | None,
    *,
    unit_style: UnitStyle = "derived",
    derived: bool | None = None,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Parse, simplify, choose a final unit representation, and format."""
    result = _apply_unit_style(
        parse_unit(value),
        unit_style=unit_style,
        derived=derived,
    )

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def multiply_units(
    *values: UnitExpr | str | None,
    unit_style: UnitStyle = "derived",
    derived: bool | None = None,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Multiply unit expressions and return the chosen representation."""
    result = UnitExpr.dimensionless()

    for value in values:
        result = result * parse_unit(value)

    result = _apply_unit_style(
        result,
        unit_style=unit_style,
        derived=derived,
    )

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def divide_units(
    numerator: UnitExpr | str | None,
    denominator: UnitExpr | str | None,
    *,
    unit_style: UnitStyle = "derived",
    derived: bool | None = None,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Divide two unit expressions and return the chosen representation."""
    result = parse_unit(numerator) / parse_unit(denominator)
    result = _apply_unit_style(
        result,
        unit_style=unit_style,
        derived=derived,
    )

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def power_unit(
    value: UnitExpr | str | None,
    power: ExponentInput,
    *,
    unit_style: UnitStyle = "derived",
    derived: bool | None = None,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Raise a unit expression to a power and return the chosen representation."""
    result = parse_unit(value) ** power
    result = _apply_unit_style(
        result,
        unit_style=unit_style,
        derived=derived,
    )

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )
