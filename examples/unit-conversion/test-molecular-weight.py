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
print(pycuc.check_reference('MOLECULAR_WEIGHT'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! molecular weight
res = pycuc.to(1, 'g/mol => kg/kmol')
print(f"1 g/mol = {res} kg/kmol")
res = pycuc.to(1, 'kg/kmol => g/mol')
print(f"1 kg/kmol = {res} g/mol")

res = pycuc.to(1, 'g/mol => kg/mol')
print(f"1 g/mol = {res} kg/mol")
res = pycuc.to(1, 'kg/mol => g/mol')
print(f"1 kg/mol = {res} g/mol")

res = pycuc.to(1, 'g/mol => mg/mol')
print(f"1 g/mol = {res} mg/mol")
res = pycuc.to(1, 'mg/mol => g/mol')
print(f"1 mg/mol = {res} g/mol")

res = pycuc.to(1, 'g/mol => g/kmol')
print(f"1 g/mol = {res} g/kmol")
res = pycuc.to(1, 'g/kmol => g/mol')
print(f"1 g/kmol = {res} g/mol")

res = pycuc.to(1, 'g/mol => lb/lbmol')
print(f"1 g/mol = {res} lb/lbmol")
res = pycuc.to(1, 'lb/lbmol => g/mol')
print(f"1 lb/lbmol = {res} g/mol")
