from fractions import Fraction

import pytest

from pycuc.algebra import (
    are_compatible,
    infer_unit_string,
    parse_unit,
    power_unit,
    simplify_unit,
)


def test_entropy_unit_expression() -> None:
    assert (
        infer_unit_string(
            "(delta_h_reaction_std - delta_g_reaction_std) / temperature",
            {
                "delta_h_reaction_std": "J/mol",
                "delta_g_reaction_std": "J/mol",
                "temperature": "K",
            },
        )
        == "J/(mol.K)"
    )


@pytest.mark.parametrize(
    ("expression", "expected"),
    [
        ("m^2/m", "m"),
        ("m/m", "dimensionless"),
        ("", "dimensionless"),
        ("None", "dimensionless"),
        ("dimensionless", "dimensionless"),
        ("J/(mol.K)", "J/(mol.K)"),
        ("mol/(m^2.s.Pa)", "mol/(m^2.s.Pa)"),
        ("(kg/m^3)^0.5", "kg^(1/2)/m^(3/2)"),
    ],
)
def test_simplify_unit(expression: str, expected: str) -> None:
    assert simplify_unit(expression) == expected


def test_non_integer_power() -> None:
    assert power_unit("m^2", 0.5) == "m"
    assert power_unit("m^3", Fraction(1, 3)) == "m"
    assert power_unit("m", 0.5) == "m^(1/2)"
    assert power_unit("m^2/s^2", 0.5) == "m/s"


def test_direct_algebra() -> None:
    assert str(parse_unit("J/mol") / parse_unit("K")) == "J/(mol.K)"
    assert str(parse_unit("m/s") ** 2) == "m^2/s^2"


def test_dimensionless_aliases() -> None:
    for value in (None, "", "None", "1", "dimensionless", "unitless"):
        assert parse_unit(value).is_dimensionless


def test_compatibility() -> None:
    assert are_compatible("J/mol", "J/mol")
    assert not are_compatible("J/mol", "K")


def test_incompatible_addition_raises() -> None:
    with pytest.raises(ValueError):
        infer_unit_string(
            "enthalpy + temperature",
            {"enthalpy": "J/mol", "temperature": "K"},
        )


def test_sqrt_expression() -> None:
    assert (
        infer_unit_string(
            "sqrt(pressure / density)",
            {
                "pressure": "kg/(m.s^2)",
                "density": "kg/m^3",
            },
        )
        == "m/s"
    )
