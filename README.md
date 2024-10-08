# Python Custom Unit Converter (PyCUC)

![Downloads](https://img.shields.io/pypi/dm/PyCUC) ![PyPI](https://img.shields.io/pypi/v/PyCUC) ![Python Version](https://img.shields.io/pypi/pyversions/PyCUC.svg) ![License](https://img.shields.io/pypi/l/PyCUC) ![Read the Docs](https://img.shields.io/readthedocs/pycuc)

Python Custom Unit Converter (PyCUC) is an open-source package designed to simplify unit conversions in Python. With PyCUC, you can effortlessly create custom conversion factors, convert between units, and streamline calculations in various fields, such as physics, engineering, and scientific computing.

**Key Features:**

* Custom Conversion Factors: Define your own conversion factors for unique units.
* Flexible Unit Conversions: Convert between units with ease, using a simple and intuitive methods.
* Lightweight: Minimal dependencies and optimized for performance.
* Easy to Use: Simple installation and straightforward usage.

## Google Colab

You can use the following code to run `PyCUC` in Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AbTCZxz9xH0VxKCh-Qhb66X0GAGo9_0y?usp=sharing)

## Installation

Install PyCUC with pip

```python
import pycuc
# check version
print(pycuc.__version__)
```

## Usage Example 1

* CHECK REFERENCES

```python
print(pycuc.check_reference('pressure'))
```

* CREATE A CUSTOM UNIT CONVERTER

```python
# ! pressure
my_cuc_1 = pycuc.create_cuc(1, 'MPa')
# convert to Pa
print(my_cuc_1.convert('Pa'))
print(my_cuc_1.convert('bar'))
print(my_cuc_1.convert('kPa'))

# ! temperature
my_cuc_2 = pycuc.create_cuc(358, 'K')
# convert to K
print(my_cuc_2.convert('C'))
print(my_cuc_2.convert('F'))
print(my_cuc_2.convert('R'))
```

* CONVERT FROM TO

```python
# ! pressure
print(pycuc.convert_from_to(1, 'MPa', 'Pa'))
# ! temperature
print(pycuc.convert_from_to(358, 'K', 'C'))
print(pycuc.convert_from_to(25, 'C', 'K'))
```

* CONVERT FROM TO (short format)

```python
# ! pressure
print(pycuc.to(125, 'MPa => Pa'))
# ! temperature
print(pycuc.to(360, 'K => C'))
print(pycuc.to(250, 'C => K'))
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

## Usage Examples 2

* LOAD `CUSTOM UNIT` FROM `YML FILES`

```python
# load unit yml file
unit_file = os.path.join(os.getcwd(), 'test', 'custom-unit.yml')
my_cuc = pycuc.go(reference_file=unit_file)
```

* `from_to` METHOD AS:

```python
# ! pressure
print(my_cuc.from_to(1, 'MPa', 'Pa'))
```

* `to` METHOD AS:

```python
# ! pressure
print(my_cuc.to(125, 'MPa => Pa'))
```

* CHECK REFERENCES:

```python
# ! from yml file
print(my_cuc.check_reference('custom::CUSTOM'))
print(my_cuc.check_reference('custom::HEAT-CAPACITY'))
print(my_cuc.check_reference('custom::ENERGY'))
```

## FAQ

For any question, contact me on [LinkedIn](https://www.linkedin.com/in/sina-gilassi/) 


## Authors

- [@sinagilassi](https://www.github.com/sinagilassi)