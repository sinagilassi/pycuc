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
# concentration
print(pycuc.check_reference('CONCENTRATION'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! concentration (mole based)
res = pycuc.to(1, 'mol/m3 => mol/L')
print(f"1 mol/m3 = {res} mol/L")
res = pycuc.to(1, 'mol/L => mol/m3')
print(f"1 mol/L = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => M')
print(f"1 mol/m3 = {res} M")
res = pycuc.to(1, 'M => mol/m3')
print(f"1 M = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => mM')
print(f"1 mol/m3 = {res} mM")
res = pycuc.to(1, 'mM => mol/m3')
print(f"1 mM = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => uM')
print(f"1 mol/m3 = {res} uM")
res = pycuc.to(1, 'uM => mol/m3')
print(f"1 uM = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => nM')
print(f"1 mol/m3 = {res} nM")
res = pycuc.to(1, 'nM => mol/m3')
print(f"1 nM = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => pM')
print(f"1 mol/m3 = {res} pM")
res = pycuc.to(1, 'pM => mol/m3')
print(f"1 pM = {res} mol/m3")

# unicode aliases
res = pycuc.to(1, '\u03BCM => mol/m3')
print(f"1 \u03BCM = {res} mol/m3")
res = pycuc.to(1, '\u00B5M => mol/m3')
print(f"1 \u00B5M = {res} mol/m3")

# mol/XXX conversions
res = pycuc.to(1, 'mol/m3 => mol/cm3')
print(f"1 mol/m3 = {res} mol/cm3")
res = pycuc.to(1, 'mol/cm3 => mol/m3')
print(f"1 mol/cm3 = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => mol/dm3')
print(f"1 mol/m3 = {res} mol/dm3")
res = pycuc.to(1, 'mol/dm3 => mol/m3')
print(f"1 mol/dm3 = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => mol/mL')
print(f"1 mol/m3 = {res} mol/mL")
res = pycuc.to(1, 'mol/mL => mol/m3')
print(f"1 mol/mL = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => mol/ft3')
print(f"1 mol/m3 = {res} mol/ft3")
res = pycuc.to(1, 'mol/ft3 => mol/m3')
print(f"1 mol/ft3 = {res} mol/m3")

# kmol basis
res = pycuc.to(1, 'kmol/m3 => mol/m3')
print(f"1 kmol/m3 = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => kmol/m3')
print(f"1 mol/m3 = {res} kmol/m3")
