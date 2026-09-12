# import packages/modules
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pycuc
from rich import print

# NOTE: avoid Windows cp1252 console errors for unicode units
_reconfigure = getattr(sys.stdout, 'reconfigure', None)
if callable(_reconfigure):
    _reconfigure(encoding='utf-8')

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
print(pycuc.check_reference('VELOCITY'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! velocity
res = pycuc.to(1, 'm/s => km/h')
print(f"1 m/s = {res} km/h")
res = pycuc.to(1, 'km/h => m/s')
print(f"1 km/h = {res} m/s")

res = pycuc.to(1, 'm/s => ft/s')
print(f"1 m/s = {res} ft/s")
res = pycuc.to(1, 'ft/s => m/s')
print(f"1 ft/s = {res} m/s")

res = pycuc.to(1, 'm/s => mph')
print(f"1 m/s = {res} mph")
res = pycuc.to(1, 'mph => m/s')
print(f"1 mph = {res} m/s")

res = pycuc.to(1, 'm/s => knot')
print(f"1 m/s = {res} knot")
res = pycuc.to(1, 'knot => m/s')
print(f"1 knot = {res} m/s")

res = pycuc.to(1, 'm/s => ft/min')
print(f"1 m/s = {res} ft/min")
res = pycuc.to(1, 'ft/min => m/s')
print(f"1 ft/min = {res} m/s")
