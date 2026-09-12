# import packages/modules
import pycuc
from rich import print

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
# gibbs free energy
print(pycuc.check_reference('GIBBS_FREE_ENERGY'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! gibbs free energy | enthalpy
print(pycuc.to(1, 'kcal/mol => J/mol'))
print(pycuc.to(1, 'kJ/mol => J/mol'))
print(pycuc.to(1, 'J/mol => kJ/mol'))
# kg/g
print(pycuc.to(1, 'J/kg => J/g'))
print(pycuc.to(1, 'kJ/kg => J/g'))
print(pycuc.to(1, 'J/g => J/kg'))
print(pycuc.to(1, 'cal/kg => kJ/g'))
