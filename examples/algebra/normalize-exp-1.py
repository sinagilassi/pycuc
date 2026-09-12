# import libs
from pycuc.utils import _normalize_conversion_unit
from rich import print


print(_normalize_conversion_unit("(J)/(mol.K)"))
# "J/mol.K"

print(_normalize_conversion_unit("J/(mol.K)"))
# "J/mol.K"

print(_normalize_conversion_unit("(kJ)/(mol.K)"))
# "kJ/mol.K"
