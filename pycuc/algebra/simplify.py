from __future__ import annotations

from .parser import parse_unit
from .unit import ExponentInput, UnitExpr


def simplify_unit(
    value: UnitExpr | str | None,
    *,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Parse, simplify, and format a unit expression."""
    return parse_unit(value).format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def multiply_units(
    *values: UnitExpr | str | None,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Multiply unit expressions and return the simplified unit."""
    result = UnitExpr.dimensionless()

    for value in values:
        result = result * parse_unit(value)

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def divide_units(
    numerator: UnitExpr | str | None,
    denominator: UnitExpr | str | None,
    *,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Divide two unit expressions and return the simplified unit."""
    return (parse_unit(numerator) / parse_unit(denominator)).format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def power_unit(
    value: UnitExpr | str | None,
    power: ExponentInput,
    *,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Raise a unit expression to an integer or non-integer power."""
    return (parse_unit(value) ** power).format(
        dimensionless=dimensionless,
        power_style=power_style,
    )
