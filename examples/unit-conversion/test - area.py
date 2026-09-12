# import packages/modules
import pycuc
import sys
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
print(pycuc.check_reference('AREA'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! area
res = pycuc.to(1, 'm2 => cm2')
print(f"1 m2 = {res} cm2")
res = pycuc.to(1, 'cm2 => m2')
print(f"1 cm2 = {res} m2")

res = pycuc.to(1, 'm2 => mm2')
print(f"1 m2 = {res} mm2")
res = pycuc.to(1, 'mm2 => m2')
print(f"1 mm2 = {res} m2")

res = pycuc.to(1, 'm2 => km2')
print(f"1 m2 = {res} km2")
res = pycuc.to(1, 'km2 => m2')
print(f"1 km2 = {res} m2")

res = pycuc.to(1, 'm2 => ft2')
print(f"1 m2 = {res} ft2")
res = pycuc.to(1, 'ft2 => m2')
print(f"1 ft2 = {res} m2")

res = pycuc.to(1, 'm2 => in2')
print(f"1 m2 = {res} in2")
res = pycuc.to(1, 'in2 => m2')
print(f"1 in2 = {res} m2")

res = pycuc.to(1, 'm2 => yd2')
print(f"1 m2 = {res} yd2")
res = pycuc.to(1, 'yd2 => m2')
print(f"1 yd2 = {res} m2")

res = pycuc.to(1, 'ha => m2')
print(f"1 ha = {res} m2")
res = pycuc.to(1, 'acre => m2')
print(f"1 acre = {res} m2")

# unicode aliases
res = pycuc.to(1, 'm\u00B2 => ft\u00B2')
print(f"1 m\u00B2 = {res} ft\u00B2")
res = pycuc.to(1, 'cm\u00B2 => m\u00B2')
print(f"1 cm\u00B2 = {res} m\u00B2")

