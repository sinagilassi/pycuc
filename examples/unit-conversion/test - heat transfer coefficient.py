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
print(pycuc.check_reference('HEAT_TRANSFER_COEFFICIENT'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! heat transfer coefficient
res = pycuc.to(1, 'W/m2.K => kW/m2.K')
print(f"1 W/m2.K = {res} kW/m2.K")
res = pycuc.to(1, 'kW/m2.K => W/m2.K')
print(f"1 kW/m2.K = {res} W/m2.K")

res = pycuc.to(1, 'W/m2.K => W/cm2.K')
print(f"1 W/m2.K = {res} W/cm2.K")
res = pycuc.to(1, 'W/cm2.K => W/m2.K')
print(f"1 W/cm2.K = {res} W/m2.K")

res = pycuc.to(1, 'W/m2.K => W/mm2.K')
print(f"1 W/m2.K = {res} W/mm2.K")
res = pycuc.to(1, 'W/mm2.K => W/m2.K')
print(f"1 W/mm2.K = {res} W/m2.K")

res = pycuc.to(1, 'W/m2.K => W/ft2.K')
print(f"1 W/m2.K = {res} W/ft2.K")
res = pycuc.to(1, 'W/ft2.K => W/m2.K')
print(f"1 W/ft2.K = {res} W/m2.K")

res = pycuc.to(1, 'W/m2.K => BTU/(hr.ft2.F)')
print(f"1 W/m2.K = {res} BTU/(hr.ft2.F)")
res = pycuc.to(1, 'BTU/(hr.ft2.F) => W/m2.K')
print(f"1 BTU/(hr.ft2.F) = {res} W/m2.K")

res = pycuc.to(1, 'W/m2.K => BTU/hr.ft2.F')
print(f"1 W/m2.K = {res} BTU/hr.ft2.F")
res = pycuc.to(1, 'BTU/hr.ft2.F => W/m2.K')
print(f"1 BTU/hr.ft2.F = {res} W/m2.K")

res = pycuc.to(1, 'W/m2.K => kcal/(hr.m2.K)')
print(f"1 W/m2.K = {res} kcal/(hr.m2.K)")
res = pycuc.to(1, 'kcal/(hr.m2.K) => W/m2.K')
print(f"1 kcal/(hr.m2.K) = {res} W/m2.K")

# unicode aliases
res = pycuc.to(1, 'W/m\u00B2.K => W/ft\u00B2.K')
print(f"1 W/m\u00B2.K = {res} W/ft\u00B2.K")
res = pycuc.to(1, 'BTU/(hr.ft\u00B2.F) => W/m\u00B2.K')
print(f"1 BTU/(hr.ft\u00B2.F) = {res} W/m\u00B2.K")

