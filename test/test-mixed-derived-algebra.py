from pycuc.algebra import divide_units, infer_unit_string, multiply_units, simplify_unit


def test_mixed_division_reduces_to_dimensionless() -> None:
    assert divide_units("N", "kg.m/s^2") == "dimensionless"
    assert simplify_unit("N.s^2/(kg.m)") == "dimensionless"


def test_mixed_multiplication_reduces_to_derived_unit() -> None:
    assert multiply_units("Pa", "m^3") == "J"


def test_expression_mixed_division_reduces_to_dimensionless() -> None:
    assert (
        infer_unit_string(
            "force / (mass * acceleration)",
            {
                "force": "N",
                "mass": "kg",
                "acceleration": "m/s^2",
            },
        )
        == "dimensionless"
    )


def test_expression_mixed_multiplication_reduces_to_energy() -> None:
    assert (
        infer_unit_string(
            "pressure * volume",
            {
                "pressure": "Pa",
                "volume": "m^3",
            },
        )
        == "J"
    )


def test_dimensionless_function_accepts_mixed_representation_ratio() -> None:
    assert (
        infer_unit_string(
            "exp(force / (mass * acceleration))",
            {
                "force": "N",
                "mass": "kg",
                "acceleration": "m/s^2",
            },
        )
        == "dimensionless"
    )


def test_raw_style_preserves_symbolic_mixed_representation() -> None:
    assert divide_units("N", "kg.m/s^2", unit_style="raw") == "N.s^2/(kg.m)"
