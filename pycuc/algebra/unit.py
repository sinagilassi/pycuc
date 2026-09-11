from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Mapping, TypeAlias


ExponentInput: TypeAlias = int | float | Fraction


def to_fraction(
    value: ExponentInput,
    *,
    max_denominator: int = 1_000_000,
) -> Fraction:
    """Normalize a unit exponent to an exact rational representation."""
    if isinstance(value, bool):
        raise TypeError("Boolean values are not valid unit exponents.")

    if isinstance(value, Fraction):
        return value

    if isinstance(value, int):
        return Fraction(value, 1)

    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("Unit exponent must be finite.")
        return Fraction(value).limit_denominator(max_denominator)

    raise TypeError("Unit exponent must be int, float, or Fraction.")


@dataclass(frozen=True)
class UnitExpr:
    """Symbolic unit expression represented by unit-symbol exponents."""

    powers: Mapping[str, Fraction]

    def __post_init__(self) -> None:
        normalized: dict[str, Fraction] = {}

        for symbol, exponent in self.powers.items():
            if not isinstance(symbol, str) or not symbol:
                raise ValueError("Unit symbols must be non-empty strings.")

            exp = to_fraction(exponent)
            if exp == 0:
                continue

            normalized[symbol] = normalized.get(symbol, Fraction(0)) + exp

        object.__setattr__(
            self,
            "powers",
            {symbol: exp for symbol, exp in normalized.items() if exp != 0},
        )

    @classmethod
    def dimensionless(cls) -> UnitExpr:
        """Create a dimensionless unit expression."""
        return cls({})

    @property
    def is_dimensionless(self) -> bool:
        """Return True when no unit dimensions remain."""
        return not self.powers

    def __mul__(self, other: UnitExpr | str | None) -> UnitExpr:
        other_expr = _coerce_unit(other)
        result = dict(self.powers)

        for symbol, exponent in other_expr.powers.items():
            result[symbol] = result.get(symbol, Fraction(0)) + exponent

        return UnitExpr(result)

    def __truediv__(self, other: UnitExpr | str | None) -> UnitExpr:
        other_expr = _coerce_unit(other)
        result = dict(self.powers)

        for symbol, exponent in other_expr.powers.items():
            result[symbol] = result.get(symbol, Fraction(0)) - exponent

        return UnitExpr(result)

    def __pow__(self, power: ExponentInput) -> UnitExpr:
        exponent = to_fraction(power)

        if exponent == 0:
            return UnitExpr.dimensionless()

        return UnitExpr(
            {
                symbol: current_power * exponent
                for symbol, current_power in self.powers.items()
            }
        )

    def reciprocal(self) -> UnitExpr:
        """Return the reciprocal unit expression."""
        return self ** -1

    def compatible_with(self, other: UnitExpr | str | None) -> bool:
        """Return whether two expressions are symbolically compatible."""
        return self == _coerce_unit(other)

    def format(
        self,
        *,
        dimensionless: str = "dimensionless",
        power_style: str = "fraction",
    ) -> str:
        """Format the normalized unit expression."""
        if self.is_dimensionless:
            return dimensionless

        if power_style not in {"fraction", "decimal"}:
            raise ValueError("power_style must be 'fraction' or 'decimal'.")

        numerator: list[str] = []
        denominator: list[str] = []

        for symbol, exponent in self.powers.items():
            if exponent > 0:
                numerator.append(_format_power(symbol, exponent, power_style))
            else:
                denominator.append(_format_power(symbol, -exponent, power_style))

        num = ".".join(numerator) if numerator else "1"

        if not denominator:
            return num

        den = ".".join(denominator)
        return f"{num}/{den}" if len(denominator) == 1 else f"{num}/({den})"

    def __str__(self) -> str:
        return self.format()


def _coerce_unit(value: UnitExpr | str | None) -> UnitExpr:
    if isinstance(value, UnitExpr):
        return value

    from .parser import parse_unit

    return parse_unit(value)


def _format_power(
    symbol: str,
    exponent: Fraction,
    power_style: str,
) -> str:
    if exponent == 1:
        return symbol

    if power_style == "decimal":
        return f"{symbol}^{float(exponent):g}"

    if exponent.denominator == 1:
        return f"{symbol}^{exponent.numerator}"

    return f"{symbol}^({exponent.numerator}/{exponent.denominator})"
