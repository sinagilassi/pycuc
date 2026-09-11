from __future__ import annotations

from fractions import Fraction
import re

from .unit import UnitExpr, to_fraction


_DIMENSIONLESS = {
    "",
    "1",
    "none",
    "dimensionless",
    "unitless",
    "-",
}

_SYMBOL_RE = re.compile(r"[A-Za-zµμ°_][A-Za-z0-9µμ°_]*")
_NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?(?:[eE][+-]?\d+)?")

_TOKEN_RE = re.compile(
    r"""
    \s*
    (
        [A-Za-zµμ°_][A-Za-z0-9µμ°_]* |
        -?\d+(?:\.\d+)?(?:[eE][+-]?\d+)? |
        [()./^]
    )
    """,
    re.VERBOSE,
)


def normalize_unit_text(value: str | None) -> str:
    """Normalize separators and dimensionless aliases before parsing."""
    if value is None:
        return ""

    text = str(value).strip()

    if text.lower() in _DIMENSIONLESS:
        return ""

    text = text.replace("·", ".")
    text = text.replace("⋅", ".")
    text = text.replace("*", ".")
    return re.sub(r"\s+", "", text)


def parse_unit(value: UnitExpr | str | None) -> UnitExpr:
    """Parse a unit string into a normalized UnitExpr."""
    if isinstance(value, UnitExpr):
        return value

    text = normalize_unit_text(value)
    if not text:
        return UnitExpr.dimensionless()

    return UnitParser(text).parse()


class UnitParser:
    """Recursive-descent parser for PyCUC unit expressions."""

    def __init__(self, text: str):
        self.tokens = self._tokenize(text)
        self.index = 0

    @staticmethod
    def _tokenize(text: str) -> list[str]:
        pos = 0
        tokens: list[str] = []

        while pos < len(text):
            match = _TOKEN_RE.match(text, pos)
            if not match:
                raise ValueError(f"Invalid unit syntax near: {text[pos:]!r}")

            tokens.append(match.group(1))
            pos = match.end()

        return tokens

    def parse(self) -> UnitExpr:
        result = self._parse_expression()

        if self.index != len(self.tokens):
            raise ValueError(f"Unexpected token: {self.tokens[self.index]!r}")

        return result

    def _peek(self) -> str | None:
        if self.index >= len(self.tokens):
            return None
        return self.tokens[self.index]

    def _consume(self, expected: str | None = None) -> str:
        token = self._peek()

        if token is None:
            raise ValueError("Unexpected end of unit expression.")

        if expected is not None and token != expected:
            raise ValueError(f"Expected {expected!r}, got {token!r}.")

        self.index += 1
        return token

    def _parse_expression(self) -> UnitExpr:
        result = self._parse_factor()

        while True:
            token = self._peek()

            if token == ".":
                self._consume(".")
                result = result * self._parse_factor()
            elif token == "/":
                self._consume("/")
                result = result / self._parse_factor()
            else:
                return result

    def _parse_factor(self) -> UnitExpr:
        result = self._parse_primary()

        if self._peek() == "^":
            self._consume("^")
            result = result ** self._parse_exponent()

        return result

    def _parse_primary(self) -> UnitExpr:
        token = self._peek()

        if token is None:
            raise ValueError("Expected unit symbol or '('.")

        if token == "(":
            self._consume("(")
            result = self._parse_expression()
            self._consume(")")
            return result

        if _SYMBOL_RE.fullmatch(token):
            self._consume()
            return UnitExpr({token: Fraction(1)})

        if token == "1":
            self._consume()
            return UnitExpr.dimensionless()

        raise ValueError(f"Expected a unit symbol or '(', got {token!r}.")

    def _parse_exponent(self) -> Fraction:
        if self._peek() == "(":
            self._consume("(")
            numerator = _parse_number_as_fraction(self._consume())

            if self._peek() == "/":
                self._consume("/")
                denominator = _parse_number_as_fraction(self._consume())

                if denominator == 0:
                    raise ValueError("Unit exponent denominator cannot be zero.")

                exponent = numerator / denominator
            else:
                exponent = numerator

            self._consume(")")
            return exponent

        return _parse_number_as_fraction(self._consume())


def _parse_number_as_fraction(token: str) -> Fraction:
    if not _NUMBER_RE.fullmatch(token):
        raise ValueError(f"Invalid exponent value: {token!r}")

    if "." in token or "e" in token.lower():
        return to_fraction(float(token))

    return Fraction(int(token), 1)
