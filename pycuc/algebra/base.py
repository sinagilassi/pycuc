from __future__ import annotations

from fractions import Fraction

from .unit import UnitExpr


_BASE_UNIT_EXPANSIONS: dict[str, UnitExpr] = {
    "N": UnitExpr({"kg": Fraction(1), "m": Fraction(1), "s": Fraction(-2)}),
    "Pa": UnitExpr({"kg": Fraction(1), "m": Fraction(-1), "s": Fraction(-2)}),
    "J": UnitExpr({"kg": Fraction(1), "m": Fraction(2), "s": Fraction(-2)}),
    "W": UnitExpr({"kg": Fraction(1), "m": Fraction(2), "s": Fraction(-3)}),
}


def expand_to_base_units(value: UnitExpr) -> UnitExpr:
    """Expand supported SI-derived symbols to SI base-unit expressions.

    The expansion is one-way and preserves powers, including fractional and
    negative powers. Symbols without a registered expansion are left intact.

    Examples
    --------
    ``N`` -> ``kg.m/s^2``
    ``Pa`` -> ``kg/(m.s^2)``
    ``J`` -> ``kg.m^2/s^2``
    ``W`` -> ``kg.m^2/s^3``
    ``N/m`` -> ``kg/s^2``
    """
    result = UnitExpr.dimensionless()

    for symbol, power in value.powers.items():
        expansion = _BASE_UNIT_EXPANSIONS.get(symbol)
        if expansion is None:
            factor = UnitExpr({symbol: power})
        else:
            factor = expansion ** power
        result = result * factor

    return result
