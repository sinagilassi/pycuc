# import packages/modules
from rich import print
import os
import sys
import math

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import pycuc


# NOTE: avoid Windows cp1252 console errors for unicode units
_reconfigure = getattr(sys.stdout, 'reconfigure', None)
if callable(_reconfigure):
    _reconfigure(encoding='utf-8')

# check version
print(pycuc.__version__)

# =====================================
# MICRO ALIAS CONVERSIONS
# =====================================
# ! each tuple is: reference, conversion block, expected result
checks = [
    # pressure
    ('PRESSURE', 'bar => ubar', 1.0e6),
    ('PRESSURE', 'bar => µbar', 1.0e6),
    ('PRESSURE', 'bar => μbar', 1.0e6),

    # concentration
    ('CONCENTRATION', 'mol/m3 => uM', 1000.0),
    ('CONCENTRATION', 'mol/m3 => µM', 1000.0),
    ('CONCENTRATION', 'mol/m3 => μM', 1000.0),
    ('CONCENTRATION', 'mol/m3 => umol/m3', 1.0e6),
    ('CONCENTRATION', 'mol/m3 => µmol/m3', 1.0e6),
    ('CONCENTRATION', 'mol/m3 => μmol/m3', 1.0e6),

    # volume
    ('VOLUME', 'm3 => uL', 1.0e9),
    ('VOLUME', 'm3 => µL', 1.0e9),
    ('VOLUME', 'm3 => μL', 1.0e9),
    ('VOLUME', 'm3 => ul', 1.0e9),
    ('VOLUME', 'm3 => µl', 1.0e9),
    ('VOLUME', 'm3 => μl', 1.0e9),

    # mass
    ('MASS', 'kg => ug', 1.0e9),
    ('MASS', 'kg => µg', 1.0e9),
    ('MASS', 'kg => μg', 1.0e9),

    # molecular weight
    ('MOLECULAR_WEIGHT', 'g/mol => ug/mol', 1.0e6),
    ('MOLECULAR_WEIGHT', 'g/mol => µg/mol', 1.0e6),
    ('MOLECULAR_WEIGHT', 'g/mol => μg/mol', 1.0e6),

    # length
    ('LENGTH', 'm => um', 1.0e6),
    ('LENGTH', 'm => µm', 1.0e6),
    ('LENGTH', 'm => μm', 1.0e6),

    # area
    ('AREA', 'm2 => um2', 1.0e12),
    ('AREA', 'm2 => µm2', 1.0e12),
    ('AREA', 'm2 => μm2', 1.0e12),

    # area per length
    ('AREA_PER_LENGTH', 'm2/m => um2/m', 1.0e12),
    ('AREA_PER_LENGTH', 'm2/m => µm2/m', 1.0e12),
    ('AREA_PER_LENGTH', 'm2/m => μm2/m', 1.0e12),

    # viscosity
    ('VISCOSITY', 'P => uP', 1.0e6),
    ('VISCOSITY', 'P => µP', 1.0e6),
    ('VISCOSITY', 'P => μP', 1.0e6),
    ('VISCOSITY', 'P => uPa.s', 1.0e5),
    ('VISCOSITY', 'P => µPa.s', 1.0e5),
    ('VISCOSITY', 'P => μPa.s', 1.0e5),

    # flow rate - mass basis
    ('FLOW_RATE', 'kg/s => ug/s', 1.0e9),
    ('FLOW_RATE', 'kg/s => µg/s', 1.0e9),
    ('FLOW_RATE', 'kg/s => μg/s', 1.0e9),
    ('FLOW_RATE', 'kg/min => ug/min', 1.0e9),
    ('FLOW_RATE', 'kg/min => µg/min', 1.0e9),
    ('FLOW_RATE', 'kg/min => μg/min', 1.0e9),

    # flow rate - volume basis
    ('FLOW_RATE', 'm3/s => uL/s', 1.0e9),
    ('FLOW_RATE', 'm3/s => µL/s', 1.0e9),
    ('FLOW_RATE', 'm3/s => μL/s', 1.0e9),
    ('FLOW_RATE', 'm3/min => uL/min', 1.0e9),
    ('FLOW_RATE', 'm3/min => µL/min', 1.0e9),
    ('FLOW_RATE', 'm3/min => μL/min', 1.0e9),
]


# =====================================
# CONVERT FROM TO (short format)
# =====================================
for reference, conversion_block, expected in checks:
    res = pycuc.to(1, conversion_block, reference=reference)
    print(f"[{reference}] 1 {conversion_block} = {res}")
    assert math.isclose(res, expected, rel_tol=1e-12)
