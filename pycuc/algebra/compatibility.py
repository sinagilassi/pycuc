from __future__ import annotations

from .base import expand_to_base_units
from .parser import parse_unit
from .unit import UnitExpr


def _normalized_base_unit(value: UnitExpr | str | None) -> UnitExpr:
    """Parse a unit and expand supported derived symbols to base dimensions."""
    return expand_to_base_units(parse_unit(value))


def are_compatible(
    left: UnitExpr | str | None,
    right: UnitExpr | str | None,
) -> bool:
    """Return whether two units are dimensionally compatible.

    Compatibility is checked after expanding supported SI-derived symbols to
    base dimensions. For example, ``N`` is compatible with ``kg.m/s^2`` and
    ``Pa`` is compatible with ``kg/(m.s^2)``.

    This layer checks dimensions only; scale-aware compatibility such as
    ``kJ/mol`` versus ``J/mol`` remains the responsibility of the conversion
    registry.
    """
    return _normalized_base_unit(left) == _normalized_base_unit(right)


def require_compatible(
    left: UnitExpr | str | None,
    right: UnitExpr | str | None,
    *,
    context: str | None = None,
) -> UnitExpr:
    """Validate dimensional compatibility and return the left-hand unit."""
    left_unit = parse_unit(left)
    right_unit = parse_unit(right)

    left_base = expand_to_base_units(left_unit)
    right_base = expand_to_base_units(right_unit)

    if left_base != right_base:
        suffix = f" for {context}" if context else ""
        raise ValueError(
            f"Incompatible units{suffix}: "
            f"{left_unit.format()!r} and {right_unit.format()!r}."
        )

    return left_unit
