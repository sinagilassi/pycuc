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

# NOTE: ODE
# ! dC/dt = -k C
print(
    infer_unit_string(
        "-k * C",
        {
            "k": "1/s",
            "C": "mol/m^3",
        },
    )
)
# mol/(m^3.s)

# NOTE: PDE
# ! m d²x/dt² + c dx/dt + k x = F
units = {
    "m": "kg",
    "d2x_dt2": "m/s^2",
    "c": "kg/s",
    "dx_dt": "m/s",
    "k": "N/m",
    "x": "m",
}

print(
    infer_unit_string(
        "m * d2x_dt2",
        units,
    )
)
# N

print(
    infer_unit_string(
        "c * dx_dt",
        units,
    )
)
# N

# ! unit style: base
print(
    infer_unit_string(
        "k * x",
        units,
        unit_style="derived"
    )
)
# N

# ! unit style: derived
print(
    infer_unit_string(
        "k * x",
        units,
        unit_style="base"
    )
)
# kg.m/s^2

print(
    infer_unit_string(
        "m * d2x_dt2 + c * dx_dt + k * x",
        units,
        unit_style="base"
    )
)
# N

# NOTE: simplification
print(
    infer_unit_string(
        "force / (mass * acceleration)",
        {
            "force": "N",
            "mass": "kg",
            "acceleration": "m/s^2",
        },
    )
)
# dimensionless
