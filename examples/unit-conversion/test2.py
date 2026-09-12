# import packages/modules
import os
import pycuc

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
print(pycuc.check_reference('pressure'))

# =====================================
# LOAD CUSTOM UNIT FROM YML
# =====================================
# load unit yml file
unit_file = os.path.join(os.getcwd(), 'test', 'custom-unit.yml')
my_cuc = pycuc.go(reference_file=unit_file)

# =====================================
# CONVERT FROM TO
# =====================================
# ! pressure
print(my_cuc.from_to(1, 'MPa', 'Pa'))
# ! temperature
print(my_cuc.from_to(358, 'K', 'C'))
print(my_cuc.from_to(25, 'C', 'K'))
print("-"*50)

# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! pressure
print(my_cuc.to(125, 'MPa => Pa'))
# ! temperature
print(my_cuc.to(360, 'K => C'))
print(my_cuc.to(250, 'C => K'))
print("-"*50)

# =====================================
# ADD A NEW UNIT
# =====================================
# ! heat capacity unit: J/mol.K
# add custom
my_cuc.add_custom_unit('J/mol.K', 1)
my_cuc.add_custom_unit('kJ/mol.K', 1000)
# conversion
print(my_cuc.from_to(150, 'J/mol.K', 'kJ/mol.K'))
print("-"*50)

# =====================================
# CHECK REFERENCE
# =====================================
# ! pressure
print(my_cuc.check_reference('pressure'))
# ! temperature
print(my_cuc.check_reference('temperature'))
# ! custom
print(my_cuc.check_reference('custom'))
# ! from yml file
print(my_cuc.check_reference('custom::CUSTOM'))
print(my_cuc.check_reference('custom::HEAT-CAPACITY'))
print(my_cuc.check_reference('custom::ENERGY'))
