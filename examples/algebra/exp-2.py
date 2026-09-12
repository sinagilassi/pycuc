# import libs
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

# NOTE: Ideal gas law unit inference
print(
    infer_unit_string(
        "n * R * T / V",
        {
            "n": "mol",
            "R": "J/(mol.K)",
            "T": "K",
            "V": "m^3",
        },
    )
)

# NOTE: Van der Waals equation unit inference
print(
    infer_unit_string(
        "n * R * T / (V - n * b)",
        {
            "n": "mol",
            "R": "J/(mol.K)",
            "T": "K",
            "V": "m^3",
            "b": "m^3/mol",
        },
    )
)

# NOTE: attraction term
print(
    infer_unit_string(
        "a * n**2 / V**2",
        {
            "a": "Pa.m^6/mol^2",
            "n": "mol",
            "V": "m^3",
        },
    )
)

# NOTE: PR term
print(
    infer_unit_string(
        "a_alpha / denominator",
        {
            "a_alpha": "Pa.m^6/mol^2",
            "denominator": "m^6/mol^2",
        },
    )
)

print(
    infer_unit_string(
        "a_alpha / (Vm * (Vm + b) + b * (Vm - b))",
        {
            "a_alpha": "Pa.m^6/mol^2",
            "Vm": "m^3/mol",
            "b": "m^3/mol",
        },
    )
)

# NOTE: thermodynamics
print(
    infer_unit_string(
        "delta_h - T * delta_s",
        {
            "delta_h": "J/mol",
            "T": "K",
            "delta_s": "J/(mol.K)",
        },
    )
)

print(
    infer_unit_string(
        "-delta_g / (R * T)",
        {
            "delta_g": "J/mol",
            "R": "J/(mol.K)",
            "T": "K",
        },
    )
)

# NOTE: density
print(
    infer_unit_string(
        "rho * velocity * length / mu",
        {
            "rho": "kg/m^3",
            "velocity": "m/s",
            "length": "m",
            "mu": "kg/(m.s)",
        },
    )
)

print(
    infer_unit_string(
        "sqrt(P / rho)",
        {
            "P": "kg/(m.s^2)",
            "rho": "kg/m^3",
        },
    )
)

print(
    infer_unit_string(
        "V ** (1/3)",
        {
            "V": "m^3",
        },
    )
)

# NOTE: heat transfer
print(
    infer_unit_string(
        "h * L / k",
        {
            "h": "W/(m^2.K)",
            "L": "m",
            "k": "W/(m.K)",
        },
    )
)

# NOTE: mass transfer
print(
    infer_unit_string(
        "kc * L / D",
        {
            "kc": "m/s",
            "L": "m",
            "D": "m^2/s",
        },
    )
)

print(
    infer_unit_string(
        "Ea / (R * T)",
        {
            "Ea": "J/mol",
            "R": "J/(mol.K)",
            "T": "K",
        },
    )
)

# NOTE: NRTL
print(
    infer_unit_string(
        "(g_ij - g_jj) / (R * T)",
        {
            "g_ij": "J/mol",
            "g_jj": "J/mol",
            "R": "J/(mol.K)",
            "T": "K",
        },
    )
)

infer_unit_string(
    "exp(-alpha * tau)",
    {
        "alpha": "dimensionless",
        "tau": "dimensionless",
    },
)

infer_unit_string(
    "exp(-energy)",
    {
        "energy": "J/mol",
    },
)
