from pycuc.algebra import infer_unit_string
from fractions import Fraction
from rich import print
from pycuc.algebra import (
    simplify_unit,
    multiply_units,
    divide_units,
    power_unit,
    parse_unit,
    infer_unit_string,
)
from pycuc import convert_from_to, from_to


# 1. Simplify a unit
print(simplify_unit("m^2/m"))
# m


# 2. Multiply units
print(multiply_units("mol/m^3", "m^3"))
# mol


# 3. Divide units
print(divide_units("J/mol", "K"))
# J/(mol.K)


# 4. Integer power
print(power_unit("m/s", 2))
# m^2/s^2


# 5. Non-integer power
print(power_unit("m^2", 0.5))
# m


# 6. Exact fractional power
print(power_unit("m^3", Fraction(1, 3)))
# m


# 7. More complex fractional power
print(power_unit("kg/m^3", 0.5))
# kg^(1/2)/m^(3/2)


# 8. Direct algebra
u = parse_unit("m^2/s^2") ** 0.5
print(u)
# m/s


# 9. Dimensionless
print(simplify_unit("mol/mol"))
# dimensionless

print(simplify_unit(""))
# dimensionless

print(simplify_unit(None))
# dimensionless


# 10. Your thermodynamic equation
result_unit = infer_unit_string(
    "(delta_h_reaction_std - delta_g_reaction_std) / temperature",
    {
        "delta_h_reaction_std": "J/mol",
        "delta_g_reaction_std": "J/mol",
        "temperature": "K",
    },
)

print(result_unit)
# J/(mol.K)


print(
    infer_unit_string(
        "(H - G) / T",
        {
            "H": "J/mol",
            "G": "J/mol",
            "T": "K",
        },
    )
)

# ! to kj
print(from_to(
    value=1,
    from_unit="J/(mol.K)",
    to_unit="kJ/(mol.K)",
))
