from __future__ import annotations

from fractions import Fraction
from typing import Mapping

from .unit import UnitExpr


# Ordered, one-way preferred SI reductions.  Rules intentionally avoid
# semantic rewrites such as s^-1 -> Hz, which are dimensionally valid but can
# obscure engineering meaning (for example first-order rate constants).
_DERIVED_RULES: tuple[tuple[Mapping[str, Fraction], str], ...] = (
    ({"J": Fraction(1), "m": Fraction(-3)}, "Pa"),
    ({"N": Fraction(1), "m": Fraction(-2)}, "Pa"),
    ({"J": Fraction(1), "s": Fraction(-1)}, "W"),
    ({"N": Fraction(1), "m": Fraction(1)}, "J"),
    ({"kg": Fraction(1), "m": Fraction(-1), "s": Fraction(-2)}, "Pa"),
    ({"kg": Fraction(1), "m": Fraction(2), "s": Fraction(-3)}, "W"),
    ({"kg": Fraction(1), "m": Fraction(2), "s": Fraction(-2)}, "J"),
    ({"kg": Fraction(1), "m": Fraction(1), "s": Fraction(-2)}, "N"),
)


def reduce_derived_unit(value: UnitExpr) -> UnitExpr:
    """Reduce composite units to preferred common SI-derived symbols.

    The reduction is symbolic and one-way, so it cannot oscillate between
    equivalent representations such as ``Pa.m^3`` and ``J``.  Existing
    derived symbols are preserved while recognizable composite factors are
    collapsed. Fractional and repeated powers are supported.

    Examples
    --------
    ``J/m^3`` -> ``Pa``
    ``N/m^2`` -> ``Pa``
    ``J/s`` -> ``W``
    ``N.m`` -> ``J``
    ``kg.m/s^2`` -> ``N``
    ``J^2/m^6`` -> ``Pa^2``
    """
    result = value

    # Several passes allow a reduction produced by one rule to participate in
    # a later rule, e.g. kg.m^2/s^2 -> J.  The rules are strictly one-way, so
    # this converges quickly.
    for _ in range(len(_DERIVED_RULES) + 1):
        changed = False
        for pattern, symbol in _DERIVED_RULES:
            reduced = _apply_rule(result, pattern, symbol)
            if reduced != result:
                result = reduced
                changed = True
        if not changed:
            break

    return result


def _apply_rule(
    value: UnitExpr,
    pattern: Mapping[str, Fraction],
    replacement: str,
) -> UnitExpr:
    """Replace the largest common power of ``pattern`` in ``value``."""
    ratios: list[Fraction] = []

    for symbol, required_power in pattern.items():
        current_power = value.powers.get(symbol, Fraction(0))

        if current_power == 0 or current_power * required_power <= 0:
            return value

        ratio = current_power / required_power
        if ratio <= 0:
            return value

        ratios.append(ratio)

    factor = min(ratios)
    if factor <= 0:
        return value

    powers = dict(value.powers)
    for symbol, required_power in pattern.items():
        new_power = powers.get(symbol, Fraction(0)) - required_power * factor
        if new_power == 0:
            powers.pop(symbol, None)
        else:
            powers[symbol] = new_power

    powers[replacement] = powers.get(replacement, Fraction(0)) + factor
    return UnitExpr(powers)
