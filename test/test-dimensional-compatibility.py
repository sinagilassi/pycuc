import pytest

from pycuc.algebra import are_compatible, infer_unit_string


def test_force_derived_and_base_units_are_compatible() -> None:
    assert are_compatible("N", "kg.m/s^2")
    assert are_compatible("kg.m/s^2", "N")


def test_pressure_derived_and_base_units_are_compatible() -> None:
    assert are_compatible("Pa", "kg/(m.s^2)")
    assert are_compatible("J/m^3", "Pa")


def test_mass_spring_damper_expression() -> None:
    assert (
        infer_unit_string(
            "m * d2x_dt2 + c * dx_dt + k * x",
            {
                "m": "kg",
                "d2x_dt2": "m/s^2",
                "c": "kg/s",
                "dx_dt": "m/s",
                "k": "N/m",
                "x": "m",
            },
            unit_style="base",
        )
        == "kg.m/s^2"
    )


def test_true_incompatibility_still_raises() -> None:
    with pytest.raises(ValueError):
        infer_unit_string(
            "force + temperature",
            {
                "force": "N",
                "temperature": "K",
            },
        )
