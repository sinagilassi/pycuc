from pycuc.algebra import infer_unit_string, simplify_unit


def test_ideal_gas_expression_reduces_to_pressure() -> None:
    assert (
        infer_unit_string(
            "n * R * T / V",
            {
                "n": "mol",
                "R": "J/(mol.K)",
                "T": "K",
                "V": "m^3",
            },
        )
        == "Pa"
    )


def test_common_si_derived_reductions() -> None:
    assert simplify_unit("J/m^3") == "Pa"
    assert simplify_unit("N/m^2") == "Pa"
    assert simplify_unit("kg/(m.s^2)") == "Pa"
    assert simplify_unit("J/s") == "W"
    assert simplify_unit("N.m") == "J"
    assert simplify_unit("kg.m/s^2") == "N"


def test_repeated_derived_power() -> None:
    assert simplify_unit("J^2/m^6") == "Pa^2"


def test_derived_reduction_can_be_disabled() -> None:
    assert simplify_unit("J/m^3", derived=False) == "J/m^3"
    assert (
        infer_unit_string(
            "n * R * T / V",
            {
                "n": "mol",
                "R": "J/(mol.K)",
                "T": "K",
                "V": "m^3",
            },
            derived=False,
        )
        == "J/m^3"
    )


def test_semantic_inverse_time_is_not_rewritten_as_hertz() -> None:
    assert simplify_unit("1/s") == "1/s"
