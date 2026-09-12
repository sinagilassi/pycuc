from __future__ import annotations

from .derived import reduce_derived_unit
from .parser import parse_unit
from .unit import ExponentInput, UnitExpr


def simplify_unit(
    value: UnitExpr | str | None,
    *,
    derived: bool = True,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Parse, simplify, optionally reduce derived SI units, and format."""
    result = parse_unit(value)
    if derived:
        result = reduce_derived_unit(result)

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def multiply_units(
    *values: UnitExpr | str | None,
    derived: bool = True,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Multiply unit expressions and return the simplified unit."""
    result = UnitExpr.dimensionless()

    for value in values:
        result = result * parse_unit(value)

    if derived:
        result = reduce_derived_unit(result)

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def divide_units(
    numerator: UnitExpr | str | None,
    denominator: UnitExpr | str | None,
    *,
    derived: bool = True,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Divide two unit expressions and return the simplified unit."""
    result = parse_unit(numerator) / parse_unit(denominator)
    if derived:
        result = reduce_derived_unit(result)

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )


def power_unit(
    value: UnitExpr | str | None,
    power: ExponentInput,
    *,
    derived: bool = True,
    dimensionless: str = "dimensionless",
    power_style: str = "fraction",
) -> str:
    """Raise a unit expression to an integer or non-integer power."""
    result = parse_unit(value) ** power
    if derived:
        result = reduce_derived_unit(result)

    return result.format(
        dimensionless=dimensionless,
        power_style=power_style,
    )
