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
print(pycuc.check_reference('LENGTH'))
length_ref = cast(
    dict[str, float],
    pycuc.check_reference('LENGTH', dataframe=False)
)
assert math.isclose(length_ref['dm'], 10.0, rel_tol=1e-12)
assert math.isclose(length_ref['um'], 1.0e6, rel_tol=1e-12)
assert math.isclose(length_ref['µm'], 1.0e6, rel_tol=1e-12)
assert math.isclose(length_ref['μm'], 1.0e6, rel_tol=1e-12)
assert math.isclose(length_ref['nm'], 1.0e9, rel_tol=1e-12)
assert math.isclose(length_ref['pm'], 1.0e12, rel_tol=1e-12)
assert math.isclose(length_ref['angstrom'], 1.0e10, rel_tol=1e-12)
assert math.isclose(length_ref['Å'], 1.0e10, rel_tol=1e-12)


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! length
res = pycuc.to(1, 'm => dm')
print(f"1 m = {res} dm")
assert math.isclose(res, 10.0, rel_tol=1e-12)
res = pycuc.to(1, 'dm => m')
print(f"1 dm = {res} m")
assert math.isclose(res, 0.1, rel_tol=1e-12)

res = pycuc.to(1, 'm => cm')
print(f"1 m = {res} cm")
assert math.isclose(res, 100.0, rel_tol=1e-12)
res = pycuc.to(1, 'cm => m')
print(f"1 cm = {res} m")
assert math.isclose(res, 0.01, rel_tol=1e-12)

res = pycuc.to(1, 'm => mm')
print(f"1 m = {res} mm")
assert math.isclose(res, 1000.0, rel_tol=1e-12)
res = pycuc.to(1, 'mm => m')
print(f"1 mm = {res} m")
assert math.isclose(res, 0.001, rel_tol=1e-12)

res = pycuc.to(1, 'm => um')
print(f"1 m = {res} um")
assert math.isclose(res, 1.0e6, rel_tol=1e-12)
res = pycuc.to(1, 'um => m')
print(f"1 um = {res} m")
assert math.isclose(res, 1.0e-6, rel_tol=1e-12)

res = pycuc.to(1, 'm => µm')
print(f"1 m = {res} µm")
assert math.isclose(res, 1.0e6, rel_tol=1e-12)
res = pycuc.to(1, 'µm => m')
print(f"1 µm = {res} m")
assert math.isclose(res, 1.0e-6, rel_tol=1e-12)

res = pycuc.to(1, 'm => μm')
print(f"1 m = {res} μm")
assert math.isclose(res, 1.0e6, rel_tol=1e-12)
res = pycuc.to(1, 'μm => m')
print(f"1 μm = {res} m")
assert math.isclose(res, 1.0e-6, rel_tol=1e-12)

res = pycuc.to(1, 'm => nm')
print(f"1 m = {res} nm")
assert math.isclose(res, 1.0e9, rel_tol=1e-12)
res = pycuc.to(1, 'nm => m')
print(f"1 nm = {res} m")
assert math.isclose(res, 1.0e-9, rel_tol=1e-12)

res = pycuc.to(1, 'm => pm')
print(f"1 m = {res} pm")
assert math.isclose(res, 1.0e12, rel_tol=1e-12)
res = pycuc.to(1, 'pm => m')
print(f"1 pm = {res} m")
assert math.isclose(res, 1.0e-12, rel_tol=1e-12)

res = pycuc.to(1, 'm => angstrom')
print(f"1 m = {res} angstrom")
assert math.isclose(res, 1.0e10, rel_tol=1e-12)
res = pycuc.to(1, 'angstrom => m')
print(f"1 angstrom = {res} m")
assert math.isclose(res, 1.0e-10, rel_tol=1e-12)

res = pycuc.to(1, 'm => km')
print(f"1 m = {res} km")
assert math.isclose(res, 0.001, rel_tol=1e-12)
res = pycuc.to(1, 'km => m')
print(f"1 km = {res} m")
assert math.isclose(res, 1000.0, rel_tol=1e-12)

res = pycuc.to(1, 'm => ft')
print(f"1 m = {res} ft")
assert math.isclose(res, 3.28084, rel_tol=1e-6)
res = pycuc.to(1, 'ft => m')
print(f"1 ft = {res} m")
assert math.isclose(res, 1 / 3.28084, rel_tol=1e-6)

res = pycuc.to(1, 'm => in')
print(f"1 m = {res} in")
assert math.isclose(res, 39.3701, rel_tol=1e-6)
res = pycuc.to(1, 'in => m')
print(f"1 in = {res} m")
assert math.isclose(res, 1 / 39.3701, rel_tol=1e-6)
