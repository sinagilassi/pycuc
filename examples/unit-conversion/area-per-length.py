# import packages/modules
from rich import print
import os
import sys
import math
from typing import cast

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
# CHECK REFERENCES
# =====================================
print(pycuc.check_reference('AREA_PER_LENGTH'))
area_per_length_ref = cast(
    dict[str, float],
    pycuc.check_reference('AREA_PER_LENGTH', dataframe=False)
)
assert math.isclose(area_per_length_ref['ft²/ft'], 3.28084, rel_tol=1e-6)
assert math.isclose(area_per_length_ref['in²/in'], 39.3701, rel_tol=1e-6)
assert math.isclose(area_per_length_ref['yd²/yd'], 1.09361, rel_tol=1e-6)
assert math.isclose(area_per_length_ref['mi²/mi'], 0.000621371, rel_tol=1e-6)


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! area per length
res = pycuc.to(1, 'm2/m => cm2/m')
print(f"1 m2/m = {res} cm2/m")
res = pycuc.to(1, 'cm2/m => m2/m')
print(f"1 cm2/m = {res} m2/m")

res = pycuc.to(1, 'm2/m => mm2/m')
print(f"1 m2/m = {res} mm2/m")
res = pycuc.to(1, 'mm2/m => m2/m')
print(f"1 mm2/m = {res} m2/m")

res = pycuc.to(1, 'm2/m => dm2/m')
print(f"1 m2/m = {res} dm2/m")
res = pycuc.to(1, 'dm2/m => m2/m')
print(f"1 dm2/m = {res} m2/m")

res = pycuc.to(1, 'm2/m => km2/m')
print(f"1 m2/m = {res} km2/m")
res = pycuc.to(1, 'km2/m => m2/m')
print(f"1 km2/m = {res} m2/m")

res = pycuc.to(1, 'm2/m => ft2/ft')
print(f"1 m2/m = {res} ft2/ft")
assert math.isclose(res, 3.28084, rel_tol=1e-6)
res = pycuc.to(1, 'ft2/ft => m2/m')
print(f"1 ft2/ft = {res} m2/m")
assert math.isclose(res, 1 / 3.28084, rel_tol=1e-6)

res = pycuc.to(1, 'm2/m => in2/in')
print(f"1 m2/m = {res} in2/in")
assert math.isclose(res, 39.3701, rel_tol=1e-6)
res = pycuc.to(1, 'in2/in => m2/m')
print(f"1 in2/in = {res} m2/m")
assert math.isclose(res, 1 / 39.3701, rel_tol=1e-6)

res = pycuc.to(1, 'm2/m => yd2/yd')
print(f"1 m2/m = {res} yd2/yd")
assert math.isclose(res, 1.09361, rel_tol=1e-6)
res = pycuc.to(1, 'yd2/yd => m2/m')
print(f"1 yd2/yd = {res} m2/m")
assert math.isclose(res, 1 / 1.09361, rel_tol=1e-6)

res = pycuc.to(1, 'm2/m => mi2/mi')
print(f"1 m2/m = {res} mi2/mi")
assert math.isclose(res, 0.000621371, rel_tol=1e-6)
res = pycuc.to(1, 'mi2/mi => m2/m')
print(f"1 mi2/mi = {res} m2/m")
assert math.isclose(res, 1 / 0.000621371, rel_tol=1e-6)
