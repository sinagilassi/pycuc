# import packages/modules
import pycuc

# check version
print(pycuc.__version__)


# =====================================
# CHECK REFERENCES
# =====================================
print(pycuc.check_reference('pressure'))

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
print("-"*50)

# =====================================
# CONVERT FROM TO (short format)
# =====================================
# ! pressure
print(pycuc.to(125, 'MPa => Pa'))
# ! temperature
print(pycuc.to(360, 'K => C'))
print(pycuc.to(250, 'C => K'))
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
# LOAD CUSTOM UNIT FROM YML
# =====================================
print(my_cuc_3.load_custom_unit('test/custom-unit.yml'))

# load from yml file
print(my_cuc_3.convert('J/kmol.K'))

# =====================================
# CHECK REFERENCE
# =====================================
# ! pressure
print(my_cuc_3.check_reference('pressure'))
# ! temperature
print(my_cuc_3.check_reference('temperature'))
# ! custom
print(my_cuc_3.check_reference('custom'))
# ! from yml file
print(my_cuc_3.check_reference('custom::HEAT-CAPACITY'))
print(my_cuc_3.check_reference('custom::ENERGY'))
