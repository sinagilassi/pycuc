# import packages/modules
import pycuc
from rich import print

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
# gibbs free energy
print(pycuc.check_reference('DENSITY'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! density
# NOTE: mass per volume
res = pycuc.to(1, 'g/cm3 => kg/m3')
print(f"1 g/cm3 = {res} kg/m3")
res = pycuc.to(1, 'kg/m3 => g/cm3')
print(f"1 kg/m3 = {res} g/cm3")
res = pycuc.to(1, 'kg/dm3 => g/cm3')
print(f"1 kg/dm3 = {res} g/cm3")
res = pycuc.to(1, 'g/cm3 => kg/dm3')
print(f"1 g/cm3 = {res} kg/dm3")
res = pycuc.to(1, 't/m3 => kg/dm3')
print(f"1 t/m3 = {res} kg/dm3")
res = pycuc.to(1, 'kg/dm3 => t/m3')
print(f"1 kg/dm3 = {res} t/m3")

# NOTE: mole per volume
res = pycuc.to(1, 'mol/L => mol/m3')
print(f"1 mol/L = {res} mol/m3")
res = pycuc.to(1, 'mol/m3 => mol/L')
print(f"1 mol/m3 = {res} mol/L")
res = pycuc.to(1, 'kmol/dm3 => kmol/m3')
print(f"1 kmol/dm3 = {res} kmol/m3")
res = pycuc.to(1, 'kmol/m3 => kmol/dm3')
print(f"1 kmol/m3 = {res} kmol/dm3")
res = pycuc.to(1, 'mol/cm3 => mol/L')
print(f"1 mol/cm3 = {res} mol/L")
res = pycuc.to(1, 'mol/L => mol/cm3')
print(f"1 mol/L = {res} mol/cm3")
