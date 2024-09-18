# CUSTOM UNIT CONVERTER
# ======================

# import packages/modules
import pandas as pd
# local


class CustomUnitConverter:
    # vars
    _pressure_conversions = {
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

    _temperature_conversions = {
        'C': 0,  # Celsius
        'F': 32,  # Fahrenheit
        'K': -273.15,  # Kelvin
        'R': 491.67  # Rankine
    }

    # Initialize empty custom conversions dictionary
    _custom_conversions = {}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def check_reference(self, reference, dataframe=True):
        '''
        Checks if the reference is valid

        Parameters
        ----------
        reference : str
            reference name such as pressure, temperature, custom

        Returns
        -------
        reference : dict | dataframe
            reference details
        '''
        try:
            # set
            reference = str(reference).strip().upper()

            # refs
            refs = {
                'PRESSURE': self._pressure_conversions,
                'TEMPERATURE': self._temperature_conversions,
                'CUSTOM': self._custom_conversions
            }

            # check
            if reference not in refs.keys():
                raise Exception('Reference not found')

            # dict
            res = refs[reference]

            if dataframe:
                # Convert dictionary to DataFrame
                df = pd.DataFrame(list(res.items()),
                                  columns=['Unit', 'Value'])
                return df
            else:
                return res
        except Exception as e:
            raise Exception('Checking references failed!, ', e)

    def find_reference(self, from_unit, to_unit):
        '''
        Finds the conversion function

        Parameters
        ----------
        from_unit : str
            from unit
        to_unit : str
            to unit

        Returns
        -------
        reference : str
            reference name such as pressure, temperature, custom
        '''
        try:
            # reference
            reference = ''
            # pressure
            if from_unit in self._pressure_conversions and to_unit in self._pressure_conversions:
                reference = 'PRESSURE'
            # temperature
            elif from_unit in self._temperature_conversions and to_unit in self._temperature_conversions:
                reference = 'TEMPERATURE'
            # custom
            elif from_unit in self._custom_conversions and to_unit in self._custom_conversions:
                reference = 'CUSTOM'
            else:
                raise Exception('Conversion units not found')

            return reference
        except Exception as e:
            raise Exception('Finding reference failed!, ', e)

    def convert(self, to_unit, reference=None):
        '''
        Selects the conversion function

        Parameters
        ----------
        reference : str
            reference name such as pressure, temperature, custom
        '''
        try:
            # find reference
            if reference is None:
                reference = self.find_reference(self.unit, to_unit)

            # upper
            reference = reference.upper()

            # reference
            ref = {
                'PRESSURE': self._pressure_conversions,
                'TEMPERATURE': self._temperature_conversions,
                'CUSTOM': self._custom_conversions
            }

            # check
            if reference not in ref.keys():
                raise Exception('Reference not found')

            # reference
            ref_methods = {
                'PRESSURE': lambda x: self.convert_pressure(x),
                'TEMPERATURE': lambda x: self.convert_temperature(x),
                'CUSTOM': lambda x: self.convert_custom(x)
            }

            # check
            if reference not in ref_methods:
                raise Exception('Reference not found')

            # set
            res = ref_methods[reference](to_unit)

            return res
        except Exception as e:
            raise Exception('Setting conversion function failed!, ', e)

    def convert_pressure(self, to_unit):
        '''
        Converts pressure from one unit to another.

        Parameters
        ----------
        to_unit : str
            to unit

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit
            # res
            return float(self.value) / float(self._pressure_conversions[from_unit]) * float(self._pressure_conversions[to_unit])
        except Exception as e:
            raise Exception('Pressure conversion failed!, ', e)

    def convert_temperature(self, to_unit):
        '''
        Converts temperature from one unit to another.

        Parameters
        ----------
        to_unit : str
            to unit

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit
            value = float(self.value)

            # Convert to Celsius first
            if from_unit == 'F':
                value = (
                    value - self._temperature_conversions[from_unit]) * 5/9
            elif from_unit == 'K':
                value = value + self._temperature_conversions[from_unit]
            elif from_unit == 'R':
                value = (
                    value - self._temperature_conversions[from_unit]) * 5/9

            # Convert from Celsius to target unit
            if to_unit == 'F':
                result = value * 9/5 + self._temperature_conversions[to_unit]
            elif to_unit == 'K':
                result = value - self._temperature_conversions[to_unit]
            elif to_unit == 'R':
                result = value * 9/5 + self._temperature_conversions[to_unit]
            else:  # to_unit == 'C'
                result = value

            return result
        except Exception as e:
            raise Exception('Temperature conversion failed!, ', e)

    def add_custom_unit(self, unit, conversion_factor):
        '''
        Adds a custom unit conversion to the reference dictionary

        Parameters
        ----------
        unit : str
            unit
        conversion_factor : float
            conversion factor

        Returns
        -------
        bool
            True if successful
        '''
        try:
            # add
            self._custom_conversions[unit] = conversion_factor
            return True
        except Exception as e:
            raise Exception('Adding new unit failed!, ', e)

    def convert_custom(self, to_unit):
        '''
        Converts using custom units

        Parameters
        ----------
        to_unit : str
            to unit

        Returns
        -------
        float
            converted value
        '''
        try:
            # set
            from_unit = self.unit

            # check
            if from_unit not in self._custom_conversions or to_unit not in self._custom_conversions:
                raise ValueError("Custom conversion units not found")

            return float(self.value) / float(self._custom_conversions[from_unit]) * float(self._custom_conversions[to_unit])
        except Exception as e:
            raise Exception('Conversion failed!, ', e)
