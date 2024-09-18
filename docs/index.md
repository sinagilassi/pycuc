# Welcome to Python Custom Unit Converter (PyCUC)

![Downloads](https://img.shields.io/pypi/dm/PyCUC) ![PyPI](https://img.shields.io/pypi/v/PyCUC) ![Python Version](https://img.shields.io/pypi/pyversions/PyCUC.svg) ![License](https://img.shields.io/pypi/l/PyCUC) 

Python Custom Unit Converter (PyCUC) is an open-source package designed to simplify unit conversions in Python. With PyCUC, you can effortlessly create custom conversion factors, convert between units, and streamline calculations in various fields, such as physics, engineering, and scientific computing.

**Key Features:**
* Custom Conversion Factors: Define your own conversion factors for unique units.
* Flexible Unit Conversions: Convert between units with ease, using a simple and intuitive methods.
* Lightweight: Minimal dependencies and optimized for performance.
* Easy to Use: Simple installation and straightforward usage.

## Installation

Install PyCUC with pip

```python
import pycuc
# check version
print(pycuc.__version__)
```

## Usage Example

* CREATE A CUSTOM UNIT CONVERTER

```python
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
```

* CONVERT FROM TO

```python
# ! pressure
print(pycuc.convert_from_to(1, 'MPa', 'Pa'))
# ! temperature
print(pycuc.convert_from_to(358, 'K', 'C'))
print(pycuc.convert_from_to(25, 'C', 'K'))
print("-"*50)
```

* DEFINE A NEW UNIT

```python
# ! heat capacity unit: J/mol.K
my_cuc_3 = pycuc.create_cuc(25, 'J/mol.K')
# add custom
my_cuc_3.add_custom_unit('J/mol.K', 1)
my_cuc_3.add_custom_unit('kJ/mol.K', 1000)
# conversion
print(my_cuc_3.convert('J/mol.K'))
print(my_cuc_3.convert('kJ/mol.K'))
print("-"*50)
```

* CHECK REFERENCE

```python
# ! pressure
print(my_cuc_3.check_reference('pressure'))
# ! temperature
print(my_cuc_3.check_reference('temperature'))
# ! custom
print(my_cuc_3.check_reference('custom'))
```

## FAQ

For any question, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/) 


## Authors

- [@sinagilassi](https://www.github.com/sinagilassi)
