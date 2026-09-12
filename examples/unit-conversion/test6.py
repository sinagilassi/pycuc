# import packages/modules
import pycuc
from rich import print

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
# gibbs free energy
print(pycuc.check_reference('VISCOSITY'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! viscosity
res = pycuc.to(1, 'cP => Pa.s')
print(f"1 cP = {res} Pa.s")
res = pycuc.to(1, 'Pa.s => cP')
print(f"1 Pa.s = {res} cP")
res = pycuc.to(1, 'mPa.s => cP')
print(f"1 mPa.s = {res} cP")
res = pycuc.to(1, 'cP => mPa.s')
print(f"1 cP = {res} mPa.s")
res = pycuc.to(1, 'P => Pa.s')
print(f"1 P = {res} Pa.s")
res = pycuc.to(1, 'Pa.s => P')
print(f"1 Pa.s = {res} P")
res = pycuc.to(1, 'μP => Pa.s')
print(f"1 μP = {res} Pa.s")
res = pycuc.to(1, 'Pa.s => μP')
print(f"1 Pa.s = {res} μP")
res = pycuc.to(1, 'g/cm.s => Pa.s')
print(f"1 g/cm.s = {res} Pa.s")
res = pycuc.to(1, 'Pa.s => g/cm.s')
print(f"1 Pa.s = {res} g/cm.s")
res = pycuc.to(1, 'N.s/m2 => Pa.s')
print(f"1 N.s/m2 = {res} Pa.s")
res = pycuc.to(1, 'Pa.s => N.s/m2')
print(f"1 Pa.s = {res} N.s/m2")
