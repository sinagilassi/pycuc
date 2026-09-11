from __future__ import annotations

from .parser import parse_unit
from .unit import UnitExpr


def are_compatible(
    left: UnitExpr | str | None,
    right: UnitExpr | str | None,
) -> bool:
    """
    Return whether two units are symbolically compatible.

    This first algebra layer compares normalized unit symbols/exponents.
    Conversion-aware compatibility (for example J/mol versus kJ/mol) should
    later delegate to PyCUC's conversion registry.
    """
    return parse_unit(left) == parse_unit(right)


def require_compatible(
    left: UnitExpr | str | None,
    right: UnitExpr | str | None,
    *,
    context: str | None = None,
) -> UnitExpr:
    """Validate compatibility and return the normalized left-hand unit."""
    left_unit = parse_unit(left)
    right_unit = parse_unit(right)

    if left_unit != right_unit:
        suffix = f" for {context}" if context else ""
        raise ValueError(
            f"Incompatible units{suffix}: "
            f"{left_unit.format()!r} and {right_unit.format()!r}."
        )

    return left_unit
