import pytest

from pycuc.algebra import infer_unit_string


def test_exp_dimensionless() -> None:
    assert (
        infer_unit_string(
            "exp(-alpha * tau)",
            {
                "alpha": "dimensionless",
                "tau": "dimensionless",
            },
        )
        == "dimensionless"
    )


def test_exp_rejects_dimensional_argument() -> None:
    with pytest.raises(ValueError, match="requires a dimensionless argument"):
        infer_unit_string("exp(-energy)", {"energy": "J/mol"})


def test_log_dimensionless() -> None:
    assert infer_unit_string("log(x)", {"x": "dimensionless"}) == "dimensionless"


def test_abs_preserves_unit() -> None:
    assert infer_unit_string("abs(x)", {"x": "J/mol"}) == "J/mol"


def test_sqrt_preserves_fractional_unit_logic() -> None:
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


def test_cbrt() -> None:
    assert infer_unit_string("cbrt(volume)", {"volume": "m^3"}) == "m"


def test_trig_requires_dimensionless_argument() -> None:
    assert infer_unit_string("sin(theta)", {"theta": "dimensionless"}) == "dimensionless"

    with pytest.raises(ValueError, match="requires a dimensionless argument"):
        infer_unit_string("sin(length)", {"length": "m"})
