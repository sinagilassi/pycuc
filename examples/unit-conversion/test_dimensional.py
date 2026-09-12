import pytest

import pycuc
from pycuc.docs.dimensional import resolve_unit_expression, validate_unit_registry
from pycuc.docs.unit_errors import (
    AffineUnitError,
    DimensionMismatchError,
    UnitSyntaxError,
)


def test_registry_is_valid_and_derived_units_reduce_recursively():
    validate_unit_registry()
    assert resolve_unit_expression("W").dimension == (1, 2, -3, 0, 0, 0, 0)
    assert resolve_unit_expression("BTU").factor_to_si == pytest.approx(1055.05585262)


@pytest.mark.parametrize(
    ("source", "target", "expected"),
    [
        ("kg.m/s^2", "N", 1),
        ("N", "kg.m/s^2", 1),
        ("kg/(m.s^2)", "Pa", 1),
        ("kg/m/s^2", "Pa", 1),
        ("Pa.s", "mPa.s", 1000),
        ("kJ/(mol.K)", "J/(mol.K)", 1000),
        ("kg.m^2/s^3", "W", 1),
        ("km", "m", 1000),
        ("M", "mol/L", 1),
        ("molal", "mol/kg", 1),
        ("(m/s)^2", "m^2/s^2", 1),
    ],
)
def test_dimensional_conversions(source, target, expected):
    assert pycuc.from_to(1, source, target) == pytest.approx(expected)


def test_heat_transfer_conversion_and_loose_denominator_style():
    assert pycuc.from_to(1, "W/(m^2.K)", "BTU/(hr.ft^2.F)") == pytest.approx(0.1761101838, rel=1e-8)
    assert pycuc.from_to(1, "BTU/hr/ft^2/F", "W/m^2/K") == pytest.approx(5.67826334, rel=1e-8)


@pytest.mark.parametrize("expression", ["", "kg..m", "kg/", "()", "(kg", "m^", "m^^2", "m^(2)"])
def test_invalid_syntax(expression):
    with pytest.raises(UnitSyntaxError):
        pycuc.from_to(1, expression, "m")


def test_unicode_superscripts_and_affine_temperature_are_rejected():
    with pytest.raises(UnitSyntaxError):
        pycuc.from_to(1, "m\u00b2", "m^2")
    with pytest.raises(AffineUnitError):
        pycuc.from_to(25, "C", "K")
    with pytest.raises(DimensionMismatchError):
        pycuc.from_to(1, "kg", "N")
