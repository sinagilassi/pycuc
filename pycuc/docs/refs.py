# REFERENCE CLASS
# ================

# import module/packages
from typing import Dict, List


# local

class Refs:

    # SECTION: Time Conversions
    _time_conversions_ref = {
        "s": 1.0,
        "ms": 1000.0,
        "us": 1_000_000.0,
        "min": 1 / 60,
        "hr": 1 / 3600,
        "day": 1.0 / 86400.0,
        "week": 1.0 / 604800.0,
        "month": 1.0 / 2.628e+6,  # approximate month (30.44 days)
        "year": 1.0 / 3.154e+7,  # approximate year (365.25 days)
    }

    # SECTION: Amount Conversions
    _amount_conversions_ref = {
        "mol": 1.0,          # ! base unit
        "kmol": 1.0e-3,
        "mmol": 1.0e3,
        # micro
        "umol": 1.0e6,      # ASCII u
        "mumol": 1.0e6,     # ASCII mu
        "μmol": 1.0e6,      # Greek mu
        "nmol": 1.0e9,
        "pmol": 1.0e12,
    }

    # SECTION: Pressure Conversions
    _pressure_conversions_ref: Dict[str, float] = {
        'bar': 1.0,
        'mbar': 1000.0,
        'ubar': 1000000.0,
        '\u00B5bar': 1000000.0,  # micro sign
        '\u03BCbar': 1000000.0,  # Greek mu
        'Pa': 100000.0,
        'hPa': 1000.0,
        'kPa': 100.0,
        'MPa': 0.1,
        'kg/cm2': 1.01972,
        'kg/cm²': 1.01972,  # with unicode
        'kg/cm^2': 1.01972,  # with caret notation
        'atm': 0.986923,
        'mmHg': 750.062,
        'mmH2O': 10197.162129779,
        'mH2O': 10.197162129779,
        'psi': 14.5038,
        'ftH2O': 33.455256555148,
        'inH2O': 401.865,
        'inHg': 29.53
    }

    # SECTION: Temperature Conversions
    _temperature_conversions_ref: Dict[str, float] = {
        'C': 0,  # Celsius
        'F': 32,  # Fahrenheit
        'K': -273.15,  # Kelvin
        'R': 491.67  # Rankine
    }

    # SECTION: Density Conversions
    _density_conversions_ref: Dict[str, float] = {
        # mass per volume
        'g/cm3': 1.0,  # ! base unit
        'g/cm³': 1.0,  # ! base unit with unicode
        'g/cm^3': 1.0,  # ! base unit with caret notation
        'kg/L': 1.0,
        'g/m3': 1000000,
        'g/m³': 1000000,  # with unicode
        'g/m^3': 1000000,  # with caret notation
        'kg/dL': 10.0,
        'g/L': 0.001,
        'g/l': 0.001,
        'g/mL': 1.0,
        'g/ml': 1.0,
        'kg/dm3': 1.0,
        'kg/dm³': 1.0,  # with unicode
        'kg/dm^3': 1.0,  # with caret notation
        't/m3': 1.0,
        't/m³': 1.0,  # with unicode
        't/m^3': 1.0,  # with caret notation
        'tonne/m3': 1.0,
        'tonne/m³': 1.0,  # with unicode
        'tonne/m^3': 1.0,  # with caret notation
        'kg/m3': 1000.0,
        'kg/m³': 1000.0,  # with unicode
        'kg/m^3': 1000.0,  # with caret notation
        'lb/ft3': 62.42796,
        'lb/ft³': 62.42796,  # with unicode
        'lb/ft^3': 62.42796,  # with caret notation
        'lb/in3': 27.6799,
        'lb/in³': 27.6799,  # with unicode
        'lb/in^3': 27.6799,  # with caret notation
        # Optional common additions
        # specific gravity (dimensionless, relative to water at 1 g/cm³)
        'sg': 1.0,
        'oz/gal': 133.526,       # US oz/gal (fluid) to g/cm³ — if needed later
        # mole per volume
        "kmol/m3": 1.0,  # ! base unit
        "kmol/m³": 1.0,  # ! base unit with unicode
        "kmol/m^3": 1.0,  # ! base unit with caret notation
        "mol/m3": 1000.0,
        "mol/m³": 1000.0,  # with unicode
        "mol/m^3": 1000.0,  # with caret notation
        "kmol/dm3": 0.001,
        "kmol/dm³": 0.001,  # with unicode
        "kmol/dm^3": 0.001,  # with caret notation
        "mol/dm3": 1.0,
        "mol/dm³": 1.0,  # with unicode
        "mol/dm^3": 1.0,  # with caret notation
        "kmol/cm3": 1e-6,
        "kmol/cm³": 1e-6,  # with unicode
        "kmol/cm^3": 1e-6,  # with caret notation
        "mol/cm3": 0.001,
        "mol/cm³": 0.001,  # with unicode
        "mol/cm^3": 0.001,  # with caret notation
        "mol/L": 1.0,
        "mol/l": 1.0,
        "M": 1.0,  # molarity shorthand
        "kmol/L": 0.001,
        "kmol/l": 0.001,
        "mol/ft3": 28.3168466,
        "mol/ft³": 28.3168466,  # with unicode
        "mol/ft^3": 28.3168466,  # with caret notation
        "kmol/ft3": 0.0283168466,
        "kmol/ft³": 0.0283168466,  # with unicode
        "kmol/ft^3": 0.0283168466,  # with caret notation
    }

    # SECTION: Concentration Conversions (mole based)
    _concentration_conversions_ref: Dict[str, float] = {
        # NOTE: base is mol/m3
        'mol/m3': 1.0,   # ! base unit
        'mol/m\u00B3': 1.0,   # ! base unit with unicode
        'mol/m^3': 1.0,   # ! base unit with caret notation
        # mol/XXX forms
        'mol/cm3': 1.0e-6,
        'mol/cm\u00B3': 1.0e-6,  # with unicode
        'mol/cm^3': 1.0e-6,  # with caret notation
        'mol/dm3': 0.001,
        'mol/dm\u00B3': 0.001,   # with unicode
        'mol/dm^3': 0.001,  # with caret notation
        'mol/L': 0.001,
        'mol/l': 0.001,
        'umol/L': 1000.0,
        'umol/l': 1000.0,
        '\u00B5mol/L': 1000.0,  # micro sign
        '\u00B5mol/l': 1000.0,  # micro sign
        '\u03BCmol/L': 1000.0,  # Greek mu
        '\u03BCmol/l': 1000.0,  # Greek mu
        'mol/mL': 1.0e-6,
        'mol/ml': 1.0e-6,
        'mol/ft3': 0.0283168466,
        'mol/ft\u00B3': 0.0283168466,  # with unicode
        'mol/ft^3': 0.0283168466,  # with caret notation
        'umol/m3': 1000000.0,
        'umol/m\u00B3': 1000000.0,
        'umol/m^3': 1000000.0,  # with caret notation
        '\u00B5mol/m3': 1000000.0,  # micro sign
        '\u00B5mol/m\u00B3': 1000000.0,  # micro sign
        '\u00B5mol/m^3': 1000000.0,  # micro sign with caret notation
        '\u03BCmol/m3': 1000000.0,  # Greek mu
        '\u03BCmol/m\u00B3': 1000000.0,  # Greek mu
        '\u03BCmol/m^3': 1000000.0,  # Greek mu with caret notation
        # kmol basis
        'kmol/m3': 0.001,
        'kmol/m\u00B3': 0.001,  # with unicode
        'kmol/m^3': 0.001,  # with caret notation
        # molarity shorthand
        'M': 0.001,
        'mM': 1.0,
        'uM': 1000.0,
        '\u03BCM': 1000.0,  # Greek mu
        '\u00B5M': 1000.0,  # micro sign
        'nM': 1.0e6,
        'pM': 1.0e9
    }

    # SECTION: Energy Conversions
    _energy_conversions_ref: Dict[str, float] = {
        'J': 1.0,
        'kJ': 0.001,
        'cal': 0.239006,
        'kcal': 0.000239006,
        'Wh': 0.000277778,
        'kWh': 2.77778e-7,
        'BTU': 0.000947817,
        'ft-lb': 0.737562
    }

    # SECTION: Energy rate Conversions
    _energy_rate_conversions_ref: Dict[str, float] = {
        'W': 1.0,
        'kW': 0.001,
        'MW': 1e-6,
        'GW': 1e-9,
        'HP': 0.00134102,
        # BTU
        'BTU/s': 0.000947817,
        'BTU/min': 0.056869,
        'BTU/h': 3.41214,
        # ft-lb
        'ft-lb/min': 0.737562,
        # cal
        'cal/s': 0.239006,
        'kcal/s': 0.000239006,
        'cal/min': 0.00398344,
        'kcal/min': 3.98344e-6,
    }

    # SECTION: Gibbs Free Energy Conversions
    _gibbs_free_energy_conversions_ref: Dict[str, float] = {
        # per mol and kmol
        'J/mol': 1.0,
        'kJ/mol': 0.001,
        'J/kmol': 1000.0,
        'cal/mol': 0.239005736,
        'kcal/mol': 0.0002390057,
        'kcal/kmol': 0.2390057,
        'cal/kmol': 239.0057,
        # per kg and g
        'J/kg': 1.0,
        'kJ/kg': 0.001,
        'cal/g': 0.000239006,
        'kcal/g': 2.39006e-7,
        'J/g': 0.001,
        'kJ/g': 1.0e-6,
        'cal/kg': 0.239006,
        'kcal/kg': 0.000239006,
    }

    # SECTION: Enthalpy Conversions
    _enthalpy_conversions_ref: Dict[str, float] = {
        # per mol and kmol
        'J/mol': 1.0,
        'kJ/mol': 0.001,
        'J/kmol': 1000.0,
        'cal/mol': 0.239005736,
        'kcal/mol': 0.0002390057,
        'kcal/kmol': 0.2390057,
        'cal/kmol': 239.0057,
        # per kg and g
        'J/kg': 1.0,
        'kJ/kg': 0.001,
        'cal/g': 0.000239006,
        'kcal/g': 2.39006e-7,
        'J/g': 0.001,
        'kJ/g': 1.0e-6,
        'cal/kg': 0.239006,
        'kcal/kg': 0.000239006,
    }

    # SECTION: Heat capacity Conversions
    _heat_capacity_conversions_ref: Dict[str, float] = {
        # mass basis
        'J/kg.K': 1.0,
        'J/kg*K': 1.0,  # with asterisk notation
        'kJ/kg.K': 0.001,
        'kJ/kg*K': 0.001,  # with asterisk notation
        'cal/kg.K': 0.239006,
        'cal/kg*K': 0.239006,  # with asterisk notation
        'kcal/kg.K': 0.000239006,
        'kcal/kg*K': 0.000239006,  # with asterisk notation
        'cal/g.K': 0.000239006,
        'cal/g*K': 0.000239006,  # with asterisk notation
        'J/g.K': 0.001,
        'J/g*K': 0.001,  # with asterisk notation
        'kJ/g.K': 1.0e-6,
        'kJ/g*K': 1.0e-6,  # with asterisk notation
        'BTU/lb.F': 0.000238846,
        'BTU/lb*F': 0.000238846,  # with asterisk notation
        # molar basis
        'J/mol.K': 1.0,
        'J/mol*K': 1.0,  # with asterisk notation
        'kJ/mol.K': 0.001,
        'kJ/mol*K': 0.001,  # with asterisk notation
        'cal/mol.K': 0.239005736,
        'cal/mol*K': 0.239005736,  # with asterisk notation
        'kcal/mol.K': 0.0002390057,
        'kcal/mol*K': 0.0002390057,  # with asterisk notation
        'cal/kmol.K': 239.0057,
        'cal/kmol*K': 239.0057,  # with asterisk notation
        'kcal/kmol.K': 0.2390057,
        'kcal/kmol*K': 0.2390057,  # with asterisk notation
        'J/kmol.K': 1000.0,
        'J/kmol*K': 1000.0,  # with asterisk notation
        'kJ/kmol.K': 1.0,
        'kJ/kmol*K': 1.0,  # with asterisk notation
    }

    _heat_transfer_coefficient_ref: Dict[str, float] = {
        # base
        'W/m2.K': 1.0,
        'W/m2*K': 1.0,  # with asterisk notation
        'W/m².K': 1.0,
        'W/m²*K': 1.0,  # with asterisk notation
        'W/m^2.K': 1.0,  # with caret notation
        'W/m^2*K': 1.0,  # with caret and asterisk notation
        'W/m2K': 1.0,
        'W/m²K': 1.0,
        'W/m^2K': 1.0,  # with caret notation

        # SI scaled
        'kW/m2.K': 0.001,
        'kW/m2*K': 0.001,  # with asterisk notation
        'kW/m².K': 0.001,
        'kW/m²*K': 0.001,  # with asterisk notation
        'kW/m^2.K': 0.001,  # with caret notation
        'kW/m^2*K': 0.001,  # with caret and asterisk notation

        # area variations
        'W/cm2.K': 1.0e-4,
        'W/cm2*K': 1.0e-4,  # with asterisk notation
        'W/cm².K': 1.0e-4,
        'W/cm²*K': 1.0e-4,  # with asterisk notation
        'W/cm^2.K': 1.0e-4,  # with caret notation
        'W/cm^2*K': 1.0e-4,  # with caret and asterisk notation
        'W/mm2.K': 1.0e-6,
        'W/mm2*K': 1.0e-6,  # with asterisk notation
        'W/mm².K': 1.0e-6,
        'W/mm²*K': 1.0e-6,  # with asterisk notation
        'W/mm^2.K': 1.0e-6,  # with caret notation
        'W/mm^2*K': 1.0e-6,  # with caret and asterisk notation
        'W/um2.K': 1.0e-12,
        'W/um2*K': 1.0e-12,  # with asterisk notation
        'W/um\u00B2.K': 1.0e-12,
        'W/um\u00B2*K': 1.0e-12,  # with asterisk notation
        'W/um^2.K': 1.0e-12,  # with caret notation
        'W/um^2*K': 1.0e-12,  # with caret and asterisk notation
        'W/\u00B5m2.K': 1.0e-12,  # micro sign
        'W/\u00B5m2*K': 1.0e-12,  # micro sign with asterisk notation
        'W/\u00B5m\u00B2.K': 1.0e-12,  # micro sign
        'W/\u00B5m\u00B2*K': 1.0e-12,  # micro sign with asterisk notation
        'W/\u00B5m^2.K': 1.0e-12,  # micro sign with caret notation
        'W/\u00B5m^2*K': 1.0e-12,  # micro sign with caret and asterisk notation
        'W/\u03BCm2.K': 1.0e-12,  # Greek mu
        'W/\u03BCm2*K': 1.0e-12,  # Greek mu with asterisk notation
        'W/\u03BCm\u00B2.K': 1.0e-12,  # Greek mu
        'W/\u03BCm\u00B2*K': 1.0e-12,  # Greek mu with asterisk notation
        'W/\u03BCm^2.K': 1.0e-12,  # Greek mu with caret notation
        'W/\u03BCm^2*K': 1.0e-12,  # Greek mu with caret and asterisk notation
        'W/ft2.K': 0.092903,
        'W/ft2*K': 0.092903,  # with asterisk notation
        'W/ft².K': 0.092903,
        'W/ft²*K': 0.092903,  # with asterisk notation
        'W/ft^2.K': 0.092903,  # with caret notation
        'W/ft^2*K': 0.092903,  # with caret and asterisk notation

        # imperial
        'BTU/(hr.ft2.F)': 0.1761101838,
        'BTU/(hr*ft2*F)': 0.1761101838,  # with asterisk notation
        'BTU/(hr.ft².F)': 0.1761101838,
        'BTU/(hr*ft²*F)': 0.1761101838,  # with asterisk notation
        'BTU/(hr.ft^2.F)': 0.1761101838,  # with caret notation
        'BTU/(hr*ft^2*F)': 0.1761101838,  # with caret and asterisk notation
        'BTU/hr.ft2.F': 0.1761101838,
        'BTU/hr*ft2*F': 0.1761101838,  # with asterisk notation
        'BTU/hr.ft^2.F': 0.1761101838,  # with caret notation
        'BTU/hr*ft^2*F': 0.1761101838,  # with caret and asterisk notation

        # thermal engineering
        'kcal/(hr.m2.K)': 0.859845,
        'kcal/(hr*m2*K)': 0.859845,  # with asterisk notation
        'kcal/(hr.m².K)': 0.859845,
        'kcal/(hr*m²*K)': 0.859845,  # with asterisk notation
        'kcal/(hr.m^2.K)': 0.859845,  # with caret notation
        'kcal/(hr*m^2*K)': 0.859845,  # with caret and asterisk notation
    }

    # SECTION: Volume Conversions
    _volume_conversions_ref: Dict[str, float] = {
        'm3': 1.0,
        'm³': 1.0,          # if you want Unicode
        'm^3': 1.0,         # with caret notation
        'L': 1000.0,
        'mL': 1000000.0,
        'ml': 1000000.0,
        'uL': 1000000000.0,
        'ul': 1000000000.0,
        '\u00B5L': 1000000000.0,  # micro sign
        '\u00B5l': 1000000000.0,  # micro sign
        '\u03BCL': 1000000000.0,  # Greek mu
        '\u03BCl': 1000000000.0,  # Greek mu
        'microliter': 1000000000.0,
        'microlitre': 1000000000.0,
        'cm3': 1000000.0,
        'cm³': 1000000.0,  # if you want Unicode
        'cm^3': 1000000.0,  # with caret notation
        'dm3': 1000.0,
        'dm³': 1000.0,  # if you want Unicode
        'dm^3': 1000.0,  # with caret notation
        'ft3': 35.3147,
        'ft³': 35.3147,  # if you want Unicode
        'ft^3': 35.3147,  # with caret notation
        'in3': 61023.7,
        'in³': 61023.7,  # if you want Unicode
        'in^3': 61023.7,  # with caret notation
        'gal(US)': 264.172,
        'gal(UK)': 219.969
    }

    # SECTION: Mass Conversions
    _mass_conversions_ref: Dict[str, float] = {
        'kg': 1.0,
        'g': 1000.0,
        'mg': 1000000.0,
        'ug': 1000000000.0,
        '\u00B5g': 1000000000.0,  # micro sign
        '\u03BCg': 1000000000.0,  # Greek mu
        'microgram': 1000000000.0,
        'lb': 2.20462,
        'oz': 35.274,
        't': 0.001,
        'st': 0.157473
    }

    # SECTION: Molecular Weight Conversions
    _molecular_weight_conversions_ref: Dict[str, float] = {
        # NOTE: base is g/mol
        'g/mol': 1.0,        # ! base unit

        # Same numerical value
        'kg/kmol': 1.0,
        'lb/lbmol': 1.0,

        # Larger unit (value decreases)
        'kg/mol': 0.001,     # 1 g/mol = 0.001 kg/mol

        # Smaller units (value increases)
        'mg/mol': 1000.0,    # 1 g/mol = 1000 mg/mol
        'ug/mol': 1000000.0,    # 1 g/mol = 1000000 ug/mol
        '\u00B5g/mol': 1000000.0,    # micro sign
        '\u03BCg/mol': 1000000.0,    # Greek mu
        'g/kmol': 1000.0,    # 1 g/mol = 1000 g/kmol

        # Imperial mass per mole
        'lb/mol': 0.00220462,   # 1 g/mol = 0.00220462 lb/mol
    }

    # SECTION: Power Conversions
    _power_conversions_ref: Dict[str, float] = {
        'W': 1.0,
        'kW': 0.001,
        'MW': 1e-6,
        'GW': 1e-9,
        'HP': 0.00134102,
        'BTU/h': 3.41214,
        'ft-lb/min': 0.737562
    }

    # SECTION: Length Conversions
    _length_conversions_ref: Dict[str, float] = {
        'm': 1.0,
        'dm': 10.0,
        'cm': 100.0,
        'mm': 1000.0,
        'um': 1.0e6,
        'µm': 1.0e6,
        'μm': 1.0e6,
        'micron': 1.0e6,
        'nm': 1.0e9,
        'pm': 1.0e12,
        'angstrom': 1.0e10,
        'Angstrom': 1.0e10,
        'Å': 1.0e10,
        'dam': 0.1,
        'hm': 0.01,
        'km': 0.001,
        'Mm': 1.0e-6,
        'Gm': 1.0e-9,
        'ft': 3.28084,
        'in': 39.3701,
        'yd': 1.09361,
        'mi': 0.000621371
    }

    # SECTION: area per length conversions
    _area_per_length_conversions_ref: Dict[str, float] = {
        'm2/m': 1.0,  # ! base unit
        'm²/m': 1.0,  # with unicode
        'm^2/m': 1.0,  # with caret notation
        'cm2/m': 10000.0,
        'cm²/m': 10000.0,  # with unicode
        'cm^2/m': 10000.0,  # with caret notation
        'mm2/m': 1.0e6,
        'mm²/m': 1.0e6,  # with unicode
        'mm^2/m': 1.0e6,  # with caret notation
        'um2/m': 1.0e12,
        'um\u00B2/m': 1.0e12,
        'um^2/m': 1.0e12,  # with caret notation
        '\u00B5m2/m': 1.0e12,  # micro sign
        '\u00B5m\u00B2/m': 1.0e12,  # micro sign
        '\u00B5m^2/m': 1.0e12,  # micro sign with caret notation
        '\u03BCm2/m': 1.0e12,  # Greek mu
        '\u03BCm\u00B2/m': 1.0e12,  # Greek mu
        '\u03BCm^2/m': 1.0e12,  # Greek mu with caret notation
        'km2/m': 1.0e-6,
        'km²/m': 1.0e-6,  # with unicode
        'km^2/m': 1.0e-6,  # with caret notation
        'dm2/m': 100.0,
        'dm²/m': 100.0,  # with unicode
        'dm^2/m': 100.0,  # with caret notation
        'ft2/ft': 3.28084,
        'ft²/ft': 3.28084,  # with unicode
        'ft^2/ft': 3.28084,  # with caret notation
        'in2/in': 39.3701,
        'in²/in': 39.3701,  # with unicode
        'in^2/in': 39.3701,  # with caret notation
        'yd2/yd': 1.09361,
        'yd²/yd': 1.09361,  # with unicode
        'yd^2/yd': 1.09361,  # with caret notation
        'mi2/mi': 0.000621371,
        'mi²/mi': 0.000621371,  # with unicode
        'mi^2/mi': 0.000621371,  # with caret notation
    }

    # SECTION: Area Conversions
    _area_conversions_ref: Dict[str, float] = {
        'm2': 1.0,  # ! base unit
        'm\u00B2': 1.0,  # with unicode
        'm^2': 1.0,  # with caret notation
        'cm2': 10000.0,
        'cm\u00B2': 10000.0,  # with unicode
        'cm^2': 10000.0,  # with caret notation
        'mm2': 1.0e6,
        'mm\u00B2': 1.0e6,  # with unicode
        'mm^2': 1.0e6,  # with caret notation
        'um2': 1.0e12,
        'um\u00B2': 1.0e12,
        'um^2': 1.0e12,  # with caret notation
        '\u00B5m2': 1.0e12,  # micro sign
        '\u00B5m\u00B2': 1.0e12,  # micro sign
        '\u00B5m^2': 1.0e12,  # micro sign with caret notation
        '\u03BCm2': 1.0e12,  # Greek mu
        '\u03BCm\u00B2': 1.0e12,  # Greek mu
        '\u03BCm^2': 1.0e12,  # Greek mu with caret notation
        'km2': 1.0e-6,
        'km\u00B2': 1.0e-6,  # with unicode
        'km^2': 1.0e-6,  # with caret notation
        'dm2': 100.0,
        'dm\u00B2': 100.0,  # with unicode
        'dm^2': 100.0,  # with caret notation
        'ft2': 10.7639,
        'ft\u00B2': 10.7639,  # with unicode
        'ft^2': 10.7639,  # with caret notation
        'in2': 1550.0031,
        'in\u00B2': 1550.0031,  # with unicode
        'in^2': 1550.0031,  # with caret notation
        'yd2': 1.19599,
        'yd\u00B2': 1.19599,  # with unicode
        'yd^2': 1.19599,  # with caret notation
        'ha': 1.0e-4,
        'hectare': 1.0e-4,
        'acre': 2.47105e-4
    }

    # SECTION: Force Conversions
    _force_conversions_ref: Dict[str, float] = {
        'N': 1.0,
        'kN': 0.001,
        'lbf': 0.224809,
        'kgf': 0.101972,
        'dyn': 100000,
        'ozf': 35.274
    }

    # SECTION: Viscosity Conversions
    _viscosity_conversions_ref: Dict[str, float] = {
        'P': 1.0,
        'cP': 100.0,
        'Pa.s': 0.1,
        'Pa*s': 0.1,  # with asterisk notation
        'mPa.s': 100.0,
        'mPa*s': 100.0,  # with asterisk notation
        'uPa.s': 100000.0,
        'uPa*s': 100000.0,  # with asterisk notation
        '\u00B5Pa.s': 100000.0,  # micro sign
        '\u00B5Pa*s': 100000.0,  # micro sign with asterisk notation
        '\u03BCPa.s': 100000.0,  # Greek mu
        '\u03BCPa*s': 100000.0,  # Greek mu with asterisk notation
        'g/cm.s': 1.0,
        'g/cm*s': 1.0,  # with asterisk notation
        'N.s/m2': 0.1,
        'N*s/m2': 0.1,  # with asterisk notation
        'N.s/m²': 0.1,
        'N*s/m²': 0.1,  # with asterisk notation
        'N.s/m^2': 0.1,  # with caret notation
        'N*s/m^2': 0.1,  # with caret and asterisk notation
        'μP': 1e6,
        'uP': 1e6,
        '\u00B5P': 1e6,  # micro sign
        '\u03BCP': 1e6,  # Greek mu
        'lb/ft.s': 0.671968,
        'lb/ft*s': 0.671968,  # with asterisk notation
        'lb/ft.h': 241.908,
        'lb/ft*h': 241.908  # with asterisk notation
    }

    # SECTION: Flow-rate Conversions
    _flow_rate_conversions_ref: Dict[str, float] = {
        # molar basis
        "mol/s": 1.0,
        "mmol/s": 1000.0,
        "kmol/s": 0.001,
        "mol/min": 60.0,
        "kmol/min": 0.06,
        "mol/h": 3600.0,
        "mol/hr": 3600.0,
        "kmol/h": 3.6,
        "kmol/hr": 3.6,
        "kmol/day": 86400.0,
        # mass basis
        "kg/s": 1.0,
        "g/s": 1000.0,
        "ug/s": 1000000000.0,
        "\u00B5g/s": 1000000000.0,  # micro sign
        "\u03BCg/s": 1000000000.0,  # Greek mu
        "kg/min": 60.0,
        "g/min": 60000.0,
        "ug/min": 60000000000.0,
        "\u00B5g/min": 60000000000.0,  # micro sign
        "\u03BCg/min": 60000000000.0,  # Greek mu
        "kg/h": 3600.0,
        "kg/hr": 3600.0,
        "g/h": 3600000.0,
        "g/hr": 3600000.0,
        "ug/h": 3600000000000.0,
        "ug/hr": 3600000000000.0,
        "\u00B5g/h": 3600000000000.0,  # micro sign
        "\u00B5g/hr": 3600000000000.0,  # micro sign
        "\u03BCg/h": 3600000000000.0,  # Greek mu
        "\u03BCg/hr": 3600000000000.0,  # Greek mu
        "tonne/s": 0.001,
        "lb/s": 453.592,
        "lbm/s": 453.592,
        "slug/s": 14.5939,
        "lbm/min": 27215.4,
        "slug/min": 875.632,
        "lbm/h": 1632924.0,
        "lbm/hr": 1632924.0,
        "slug/h": 52537.9,
        "slug/hr": 52537.9,
        "tonne/day": 86.4,
        "lbm/day": 39.4624e6,
        "slug/day": 1260912.0,
        "tonne/h": 3.6,
        "tonne/hr": 3.6,
        # volume basis
        "m3/s": 1.0,
        "m³/s": 1.0,          # if you want Unicode
        "m^3/s": 1.0,         # with caret notation
        "L/s": 1000.0,
        "l/s": 1000.0,
        "cm3/s": 1e6,
        "cm³/s": 1e6,        # if you want Unicode
        "cm^3/s": 1e6,       # with caret notation
        "mL/s": 1e6,
        "uL/s": 1e9,
        "ul/s": 1e9,
        "\u00B5L/s": 1e9,  # micro sign
        "\u00B5l/s": 1e9,  # micro sign
        "\u03BCL/s": 1e9,  # Greek mu
        "\u03BCl/s": 1e9,  # Greek mu
        "m3/min": 60.0,
        "m³/min": 60.0,      # if you want Unicode
        "m^3/min": 60.0,     # with caret notation
        "L/min": 60000.0,
        "l/min": 60000.0,
        "mL/min": 6e7,
        "uL/min": 6e10,
        "ul/min": 6e10,
        "\u00B5L/min": 6e10,  # micro sign
        "\u00B5l/min": 6e10,  # micro sign
        "\u03BCL/min": 6e10,  # Greek mu
        "\u03BCl/min": 6e10,  # Greek mu
        "m3/h": 3600.0,
        "m³/h": 3600.0,      # if you want Unicode
        "m^3/h": 3600.0,     # with caret notation
        "m3/hr": 3600.0,
        "m³/hr": 3600.0,      # if you want Unicode
        "m^3/hr": 3600.0,     # with caret notation
        "L/h": 3600000.0,
        "L/hr": 3600000.0,
        "l/h": 3600000.0,
        "l/hr": 3600000.0,
        "mL/h": 3.6e9,
        "uL/h": 3.6e12,
        "uL/hr": 3.6e12,
        "ul/h": 3.6e12,
        "ul/hr": 3.6e12,
        "\u00B5L/h": 3.6e12,  # micro sign
        "\u00B5L/hr": 3.6e12,  # micro sign
        "\u00B5l/h": 3.6e12,  # micro sign
        "\u00B5l/hr": 3.6e12,  # micro sign
        "\u03BCL/h": 3.6e12,  # Greek mu
        "\u03BCL/hr": 3.6e12,  # Greek mu
        "\u03BCl/h": 3.6e12,  # Greek mu
        "\u03BCl/hr": 3.6e12,  # Greek mu
        "ft3/s": 35.3147,
        "ft³/s": 35.3147,      # if you want Unicode
        "ft^3/s": 35.3147,     # with caret notation
        "ft3/min": 2118.88,
        "ft³/min": 2118.88,    # if you want Unicode
        "ft^3/min": 2118.88,   # with caret notation
        "ft3/h": 127132.8,
        "ft³/h": 127132.8,     # if you want Unicode
        "ft^3/h": 127132.8,    # with caret notation
        "ft3/hr": 127132.8,
        "ft³/hr": 127132.8,     # if you want Unicode
        "ft^3/hr": 127132.8,    # with caret notation
        "gal/s": 264.172,
        "gal/min": 15850.3,
        "bbl/day": 1.84013e-6,   # slightly more precise
        "barrel/day": 1.84013e-6,
    }

    # SECTION: Velocity Conversions
    _velocity_conversions_ref: Dict[str, float] = {
        # NOTE: base is m/s
        'm/s': 1.0,        # ! base unit
        'm/sec': 1.0,
        'cm/s': 100.0,
        'cm/sec': 100.0,
        'mm/s': 1000.0,
        'mm/sec': 1000.0,
        'km/s': 0.001,
        'km/sec': 0.001,
        'm/min': 60.0,
        'm/h': 3600.0,
        'm/hr': 3600.0,
        'km/min': 0.06,
        'km/h': 3.6,
        'km/hr': 3.6,
        'ft/s': 3.28084,
        'ft/sec': 3.28084,
        'ft/min': 196.8504,
        'ft/h': 11811.024,
        'ft/hr': 11811.024,
        'in/s': 39.3701,
        'in/sec': 39.3701,
        'mph': 2.23694,
        'mi/h': 2.23694,
        'mi/hr': 2.23694,
        'knot': 1.94384,
        'kn': 1.94384,
    }

    # SECTION: Reference
    _reference = {
        'TIME': _time_conversions_ref,
        'AMOUNT': _amount_conversions_ref,
        'PRESSURE': _pressure_conversions_ref,
        'TEMPERATURE': _temperature_conversions_ref,
        'DENSITY': _density_conversions_ref,
        'CONCENTRATION': _concentration_conversions_ref,
        'ENERGY': _energy_conversions_ref,
        'ENERGY_RATE': _energy_rate_conversions_ref,
        'GIBBS_FREE_ENERGY': _gibbs_free_energy_conversions_ref,
        'ENTHALPY': _enthalpy_conversions_ref,
        'HEAT_CAPACITY': _heat_capacity_conversions_ref,
        'HEAT_TRANSFER_COEFFICIENT': _heat_transfer_coefficient_ref,
        'VOLUME': _volume_conversions_ref,
        'MASS': _mass_conversions_ref,
        'MOLECULAR_WEIGHT': _molecular_weight_conversions_ref,
        'POWER': _power_conversions_ref,
        'LENGTH': _length_conversions_ref,
        'AREA_PER_LENGTH': _area_per_length_conversions_ref,
        'AREA': _area_conversions_ref,
        'FORCE': _force_conversions_ref,
        'VISCOSITY': _viscosity_conversions_ref,
        'FLOW_RATE': _flow_rate_conversions_ref,
        'VELOCITY': _velocity_conversions_ref
    }

    def __init__(self):
        pass

    @property
    def time_conversions_ref(self):
        return self._time_conversions_ref

    @property
    def amount_conversions_ref(self):
        return self._amount_conversions_ref

    @property
    def pressure_conversions_ref(self):
        return self._pressure_conversions_ref

    @property
    def temperature_conversions_ref(self):
        return self._temperature_conversions_ref

    @property
    def density_conversions_ref(self):
        return self._density_conversions_ref

    @property
    def concentration_conversions_ref(self):
        return self._concentration_conversions_ref

    @property
    def energy_conversions_ref(self):
        return self._energy_conversions_ref

    @property
    def energy_rate_conversions_ref(self):
        return self._energy_rate_conversions_ref

    @property
    def gibbs_free_energy_conversions_ref(self):
        return self._gibbs_free_energy_conversions_ref

    @property
    def enthalpy_conversions_ref(self):
        return self._enthalpy_conversions_ref

    @property
    def heat_capacity_conversions_ref(self):
        return self._heat_capacity_conversions_ref

    @property
    def heat_transfer_coefficient_ref(self):
        return self._heat_transfer_coefficient_ref

    @property
    def volume_conversions_ref(self):
        return self._volume_conversions_ref

    @property
    def mass_conversions_ref(self):
        return self._mass_conversions_ref

    @property
    def molecular_weight_conversions_ref(self):
        return self._molecular_weight_conversions_ref

    @property
    def power_conversions_ref(self):
        return self._power_conversions_ref

    @property
    def length_conversions_ref(self):
        return self._length_conversions_ref

    @property
    def area_per_length_conversions_ref(self):
        return self._area_per_length_conversions_ref

    @property
    def area_conversions_ref(self):
        return self._area_conversions_ref

    @property
    def force_conversions_ref(self):
        return self._force_conversions_ref

    @property
    def viscosity_conversions_ref(self):
        return self._viscosity_conversions_ref

    @property
    def flow_rate_conversions_ref(self):
        return self._flow_rate_conversions_ref

    @property
    def velocity_conversions_ref(self):
        return self._velocity_conversions_ref

    @staticmethod
    def get_reference():
        return Refs._reference

    @staticmethod
    def get_reference_by_key(key: str):
        reference = Refs.get_reference()
        return reference.get(key, None)

    @staticmethod
    def get_reference_units_by_key(key: str) -> List[str]:
        reference = Refs.get_reference()
        ref = reference.get(key, None)
        if ref is not None:
            return list(ref.keys())
        else:
            return []

    @staticmethod
    def get_all_reference_units() -> List[str]:
        reference = Refs.get_reference()
        all_units = []
        for key, ref in reference.items():
            all_units.extend(list(ref.keys()))
        return all_units

    @staticmethod
    def is_unit_in_reference(unit: str) -> bool:
        all_units = Refs.get_all_reference_units()
        # lowercase
        all_units = [u.lower() for u in all_units]
        unit = unit.lower()
        return unit in all_units

    @staticmethod
    def is_unit_in_reference_by_key(
        unit: str,
        key: str
    ) -> bool:
        units = Refs.get_reference_units_by_key(key)
        # lowercase
        units = [u.lower() for u in units]
        unit = unit.lower()
        return unit in units
