# import packages/modules
import pycuc

# check version
print(pycuc.__version__)

# =====================================
# CHECK REFERENCES
# =====================================
print(pycuc.check_reference('PRESSURE'))

# =====================================
# CREATE A CUSTOM UNIT CONVERTER
# =====================================
# ! pressure
my_cuc_1 = pycuc.create_cuc(1, 'MPa')
# convert to Pa
print(my_cuc_1.convert('Pa'))
print(my_cuc_1.convert('bar'))
print(my_cuc_1.convert('kPa'))
print("-"*50)

# ! temperature
my_cuc_2 = pycuc.create_cuc(358, 'K')
# convert to K
print(my_cuc_2.convert('C'))
print(my_cuc_2.convert('F'))
print(my_cuc_2.convert('R'))
print("-"*50)

# =====================================
# CONVERT FROM TO
# =====================================
# ! pressure
print(pycuc.convert_from_to(1, 'MPa', 'Pa'))
# ! temperature
print(pycuc.convert_from_to(358, 'K', 'C'))
print(pycuc.convert_from_to(25, 'C', 'K'))
# same unit test
print(pycuc.convert_from_to(275, 'K', 'K'))
print("-"*50)

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

# =====================================
# ADD A NEW UNIT
# =====================================
# ! heat capacity unit: J/mol.K
my_cuc_3 = pycuc.create_cuc(25, 'J/mol.K')
# add custom
my_cuc_3.add_custom_unit('J/mol.K', 1)
my_cuc_3.add_custom_unit('kJ/mol.K', 1000)
# conversion
# print(my_cuc_3.convert('J/mol.K'))
# print(my_cuc_3.convert('kJ/mol.K'))
print("-"*50)

# =====================================
# CHECK REFERENCE
# =====================================
# ! pressure
print(my_cuc_3.check_reference('PRESSURE'))
# ! temperature
print(my_cuc_3.check_reference('TEMPERATURE'))
# ! custom
print(my_cuc_3.check_reference('CUSTOM'))
