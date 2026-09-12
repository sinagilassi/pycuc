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
print(pycuc.check_reference('ENERGY_RATE'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! energy rate
res = pycuc.to(1, 'W => kW')
print(f"1 W = {res} kW")
res = pycuc.to(1, 'kW => W')
print(f"1 kW = {res} W")

res = pycuc.to(1, 'W => MW')
print(f"1 W = {res} MW")
res = pycuc.to(1, 'MW => W')
print(f"1 MW = {res} W")

res = pycuc.to(1, 'W => GW')
print(f"1 W = {res} GW")
res = pycuc.to(1, 'GW => W')
print(f"1 GW = {res} W")

res = pycuc.to(1, 'W => HP')
print(f"1 W = {res} HP")
res = pycuc.to(1, 'HP => W')
print(f"1 HP = {res} W")

res = pycuc.to(1, 'W => BTU/h')
print(f"1 W = {res} BTU/h")
res = pycuc.to(1, 'BTU/h => W')
print(f"1 BTU/h = {res} W")

res = pycuc.to(1, 'W => ft-lb/min')
print(f"1 W = {res} ft-lb/min")
res = pycuc.to(1, 'ft-lb/min => W')
print(f"1 ft-lb/min = {res} W")
