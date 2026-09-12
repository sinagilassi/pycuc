# import libs
import logging

# NOTE: setup logger
logger = logging.getLogger(__name__)


def _normalize_conversion_unit(unit: str) -> str:
    unit = unit.strip()

    # Remove redundant outer grouping on numerator:
    # (J)/(mol.K) -> J/(mol.K)
    if unit.startswith("("):
        close_idx = unit.find(")")
        if close_idx != -1 and close_idx + 1 < len(unit) and unit[close_idx + 1] == "/":
            unit = unit[1:close_idx] + unit[close_idx + 1:]

    # Remove redundant grouping on denominator:
    # J/(mol.K) -> J/mol.K
    if "/(" in unit and unit.endswith(")"):
        numerator, denominator = unit.split("/(", 1)
        unit = numerator + "/" + denominator[:-1]

    return unit
