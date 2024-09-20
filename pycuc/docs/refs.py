# REFERENCE CLASS
# ================

# import module/packages


# local

class Refs:

    # vars
    _pressure_conversions_ref = {
        'bar': 1.0,
        'mbar': 1000.0,
        'ubar': 1000000.0,
        'Pa': 100000.0,
        'hPa': 1000.0,
        'kPa': 100.0,
        'MPa': 0.1,
        'kgcm2': 1.01972,
        'atm': 0.986923,
        'mmHg': 750.062,
        'mmH2O': 10197.162129779,
        'mH2O': 10.197162129779,
        'psi': 14.5038,
        'ftH2O': 33.455256555148,
        'inH2O': 401.865,
        'inHg': 29.53
    }

    _temperature_conversions_ref = {
        'C': 0,  # Celsius
        'F': 32,  # Fahrenheit
        'K': -273.15,  # Kelvin
        'R': 491.67  # Rankine
    }

    def __init__(self):
        pass

    @property
    def pressure_conversions_ref(self):
        return self._pressure_conversions_ref

    @property
    def temperature_conversions_ref(self):
        return self._temperature_conversions_ref
