# import packages/modules
from rich import print
from pycuc.docs import Refs
import pycuc
import os
import sys
import re
import random
import math

sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))


# NOTE: avoid Windows cp1252 console errors for unicode units
_reconfigure = getattr(sys.stdout, 'reconfigure', None)
if callable(_reconfigure):
    _reconfigure(encoding='utf-8')

# check version
print(pycuc.__version__)

# =====================================
# FIND POWER-NOTATION VARIANTS (e.g. cm3 / cm^3 / cm\u00B3)
# =====================================
_SUPERSCRIPTS = {'2': '\u00B2', '3': '\u00B3'}


def find_power_variants(units):
    '''Find unit triplets, e.g. (cm3, cm^3, cm\u00B3), that denote the same unit'''
    variants = []
    for unit in units:
        m = re.search(r'(2|3)(?!\d)', unit)
        if not m:
            continue
        idx, digit = m.start(), m.group(1)
        caret_unit = unit[:idx] + '^' + unit[idx:]
        unicode_unit = unit[:idx] + _SUPERSCRIPTS[digit] + unit[idx + 1:]
        if caret_unit in units and unicode_unit in units:
            variants.append((unit, caret_unit, unicode_unit))
    return variants


# collect triplets across every reference category
reference = Refs.get_reference()
all_triplets = [
    (category, *triplet)
    for category, ref in reference.items()
    for triplet in find_power_variants(list(ref.keys()))
]
print(f"found {len(all_triplets)} power-notation triplets")

# =====================================
# RANDOMLY CHECK POWER-NOTATION UNITS ARE EQUIVALENT
# =====================================
for _ in range(10):
    category, digit_unit, caret_unit, unicode_unit = random.choice(
        all_triplets)
    value = round(random.uniform(1, 1000), 2)

    # pick a random source unit, different from the target family, from the same category
    source_units = [
        u for u in reference[category].keys()
        if u not in (digit_unit, caret_unit, unicode_unit)
    ]
    source_unit = random.choice(source_units)

    res_digit = pycuc.to(value, f'{source_unit} => {digit_unit}', category)
    res_caret = pycuc.to(value, f'{source_unit} => {caret_unit}', category)
    res_unicode = pycuc.to(value, f'{source_unit} => {unicode_unit}', category)

    match = (
        math.isclose(res_digit, res_caret, rel_tol=1e-9) and
        math.isclose(res_digit, res_unicode, rel_tol=1e-9)
    )

    print(
        f"[{category}] {value} {source_unit} => "
        f"{digit_unit}={res_digit}, {caret_unit}={res_caret}, {unicode_unit}={res_unicode} "
        f"-> {'MATCH' if match else 'MISMATCH'}"
    )
    assert match, f"Mismatch for {digit_unit}/{caret_unit}/{unicode_unit}"
