# import packages/modules
import pycuc
from rich import print

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
print(pycuc.check_reference('PRESSURE'))
print(pycuc.check_reference('TEMPERATURE'))
print(pycuc.check_reference('DENSITY'))
print(pycuc.check_reference('ENERGY'))
print(pycuc.check_reference('GIBBS_FREE_ENERGY'))
print(pycuc.check_reference('HEAT_CAPACITY'))
print(pycuc.check_reference('VOLUME'))
print(pycuc.check_reference('MASS'))
print(pycuc.check_reference('POWER'))
print(pycuc.check_reference('LENGTH'))
print(pycuc.check_reference('FORCE'))


# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! pressure
print(pycuc.to(125, 'MPa => Pa'))
# ! temperature
print(pycuc.to(360, 'K => C'))
print(pycuc.to(250, 'C => K'))
# same unit test
print(pycuc.to(275, 'K => K'))
print("-"*50)

# ! density
print(pycuc.to(1, 'g/cm3 => kg/m3'))
print(pycuc.to(1, 'g/cm³ => g/m3'))
# ! energy
print(pycuc.to(1, 'kcal => J'))
# ! heat capacity
print(pycuc.to(1, 'J/kg.K => kJ/kg.K'))
# ! volume
print(pycuc.to(1, 'L => m3'))
# ! mass
print(pycuc.to(1, 'kg => g'))
# ! power
print(pycuc.to(1, 'kW => W'))
# ! length
print(pycuc.to(1, 'cm => m'))
# ! force
print(pycuc.to(1, 'N => kN'))
