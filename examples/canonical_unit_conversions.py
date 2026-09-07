"""Check PyCUC canonical chemical-engineering unit helpers.

Run with:

    python examples/canonical_unit_conversions.py

Each case prints the conversion and asserts the expected result.
"""

from math import isclose

from pycuc.canonical import *


def check(name: str, actual: float, expected: float, rel_tol: float = 1e-10) -> None:
    ok = isclose(actual, expected, rel_tol=rel_tol, abs_tol=1e-12)
    status = "PASS" if ok else "FAIL"
    print(f"{status:4s} | {name:28s} | actual={actual:.12g} | expected={expected:.12g}")
    assert ok, f"{name} failed: {actual!r} != {expected!r}"


def main() -> None:
    # Base/general quantities
    check("to_K", to_K(25.0, "C"), 298.15)
    check("to_Pa", to_Pa(1.0, "bar"), 100000.0)
    check("to_bar", to_bar(1.0, "Pa"), 1.0e-5)
    check("to_m", to_m(100.0, "cm"), 1.0)
    check("to_m2", to_m2(10000.0, "cm^2"), 1.0)
    check("to_m3", to_m3(1000.0, "L"), 1.0)
    check("to_kg", to_kg(1000.0, "g"), 1.0)
    check("to_mol", to_mol(1.0, "kmol"), 1000.0)
    check("to_s", to_s(1.0, "hr"), 3600.0)
    check("to_J", to_J(1.0, "kJ"), 1000.0)
    check("to_W", to_W(1.0, "kW"), 1000.0)

    # Density/composition/amount quantities
    check("to_kg_per_m3", to_kg_per_m3(1.0, "g/cm^3"), 1000.0)
    check("to_mol_per_m3", to_mol_per_m3(1.0, "mol/L"), 1000.0)
    check("to_mol_per_kg", to_mol_per_kg(1.0, "mmol/g"), 1.0)
    check("to_kg_per_mol", to_kg_per_mol(18.0, "g/mol"), 0.018)
    check("to_m3_per_mol", to_m3_per_mol(1.0, "L/mol"), 0.001)
    check("to_m3_per_kg", to_m3_per_kg(1.0, "L/kg"), 0.001)

    # Process flows
    check("to_kg_per_s", to_kg_per_s(3600.0, "kg/hr"), 1.0)
    check("to_mol_per_s", to_mol_per_s(3.6, "kmol/hr"), 1.0)
    check("to_m3_per_s", to_m3_per_s(3600.0, "m^3/hr"), 1.0)
    check("to_m_per_s", to_m_per_s(3.6, "km/hr"), 1.0)

    # Thermodynamic quantities
    check("to_J_per_mol", to_J_per_mol(1.0, "kJ/mol"), 1000.0)
    check("to_J_per_kg", to_J_per_kg(1.0, "kJ/kg"), 1000.0)
    check("to_J_per_mol_K", to_J_per_mol_K(1.0, "kJ/(mol.K)"), 1000.0)
    check("to_J_per_kg_K", to_J_per_kg_K(1.0, "kJ/(kg.K)"), 1000.0)

    # Transport properties
    check("to_Pa_s", to_Pa_s(1.0, "cP"), 0.001)
    check("to_m2_per_s", to_m2_per_s(1.0, "cSt"), 1.0e-6)
    check("to_W_per_m_K", to_W_per_m_K(1.0, "kW/(m.K)"), 1000.0)
    check("to_W_per_m2_K", to_W_per_m2_K(1.0, "kW/(m^2.K)"), 1000.0)

    # Flux / reaction / membrane quantities
    check("to_mol_per_m2_s", to_mol_per_m2_s(1.0, "mmol/(cm^2.s)"), 10.0)
    check("to_kg_per_m2_s", to_kg_per_m2_s(1.0, "g/(cm^2.s)"), 10.0)
    check("to_mol_per_m3_s", to_mol_per_m3_s(1.0, "mol/(L.s)"), 1000.0)
    check(
        "to_mol_per_m2_s_Pa",
        to_mol_per_m2_s_Pa(1.0, "mmol/(m^2.s.kPa)"),
        1.0e-6,
    )

    print("\nAll canonical conversion checks passed.")


if __name__ == "__main__":
    main()
