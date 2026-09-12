import pytest

from pycuc.algebra import infer_unit_string, simplify_unit


def test_derived_style_is_default() -> None:
    assert (
        infer_unit_string(
            "k * x",
            {
                "k": "N/m",
                "x": "m",
            },
        )
        == "N"
    )


def test_base_style_expands_force() -> None:
    assert (
        infer_unit_string(
            "k * x",
            {
                "k": "N/m",
                "x": "m",
            },
            unit_style="base",
        )
        == "kg.m/s^2"
    )


def test_base_style_expands_common_derived_units() -> None:
    assert simplify_unit("N", unit_style="base") == "kg.m/s^2"
    assert simplify_unit("Pa", unit_style="base") == "kg/(m.s^2)"
    assert simplify_unit("J", unit_style="base") == "kg.m^2/s^2"
    assert simplify_unit("W", unit_style="base") == "kg.m^2/s^3"


def test_base_style_handles_composite_units() -> None:
    assert simplify_unit("N/m", unit_style="base") == "kg/s^2"
    assert simplify_unit("Pa.m^3", unit_style="base") == "kg.m^2/s^2"


def test_raw_style_preserves_symbolic_result() -> None:
    assert simplify_unit("J/m^3", unit_style="raw") == "J/m^3"


def test_backward_compatible_derived_flag() -> None:
    assert simplify_unit("J/m^3", derived=True) == "Pa"
    assert simplify_unit("J/m^3", derived=False) == "J/m^3"


def test_invalid_unit_style_raises() -> None:
    with pytest.raises(ValueError):
        simplify_unit("N", unit_style="invalid")  # type: ignore[arg-type]
