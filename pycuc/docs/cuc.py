# CUSTOM UNIT CONVERTER
# ======================

# import packages/modules
import pandas as pd
# local
from .utils import Utils
from .refs import Refs


class CustomUnitConverter(Utils, Refs):
    # vars
    # pressure
    _pressure_conversions = {}
    # temperature
    _temperature_conversions = {}

    # Initialize empty custom conversions dictionary
    _custom_conversions = {}

    # load conversion unit
    _custom_conversions_full = {
        'CUSTOM': _custom_conversions
    }

    def __init__(self, value, unit, reference_file=''):
        self.value = value
        self.unit = str(unit).strip()
        self.reference_file = reference_file
        # utils init
        super().__init__()
        Refs().__init__()

        # init vars
        self._pressure_conversions = self.pressure_conversions_ref
        self._temperature_conversions = self.temperature_conversions_ref

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

            # sub reference
            sub_reference = None
            if '::' in reference:
                # split
                reference_split = reference.split('::')
                # set
                reference = reference_split[1]
                sub_reference = reference

            # refs
            refs = {
                'PRESSURE': self._pressure_conversions,
                'TEMPERATURE': self._temperature_conversions,
                'CUSTOM': self._custom_conversions_full
            }

            # take all keys
            custom_keys = list(self._custom_conversions_full.keys())
            # all keys
            all_keys = list(set(list(refs.keys()) + custom_keys))

            # check
            if reference not in all_keys:
                raise Exception('Reference not found')

            # if contain ::
            if sub_reference:
                # set
                res = self._custom_conversions_full[sub_reference]
            elif reference == 'CUSTOM':
                res = self._custom_conversions_full['CUSTOM']
            else:
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
            reference = None
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
                # check
                for key, value in self._custom_conversions_full.items():
                    if from_unit in value and to_unit in value:
                        reference = 'CUSTOM'

            # check
            if reference is None:
                raise Exception('Conversion units not found')

            return reference
        except Exception as e:
            raise Exception('Finding reference failed!, ', e)

    def check_conversion_block(self, conversion_block):
        '''
        Checks conversion block

        Parameters
        ----------
        conversion_block : str
            conversion block

        Returns
        -------
        subgroups : list
            list of subgroups. [0] = from_unit, [1] = '=>', [2] = to_unit
        '''
        try:
            return self.parse_conversion_block(conversion_block)
        except Exception as e:
            raise Exception("Checking conversion block failed!, ", e)

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

    def load_custom_unit(self, f):
        '''
        Load custom unit

        Parameters
        ----------
        f : str
            yml file path

        Returns
        -------
        dict
            custom unit
        '''
        try:
            # custom unit
            custom_unit = self._load_custom_conversion_unit(f)

            # if not empty
            if len(custom_unit) == 0:
                return False

            # check key 'CUSTOM-UNIT'
            if 'CUSTOM-UNIT' not in custom_unit.keys():
                raise ValueError("Key 'CUSTOM-UNIT' not found")

            # update custom conversion
            for key, value in custom_unit['CUSTOM-UNIT'].items():
                self._custom_conversions_full[str(key).strip()] = value

            return self._custom_conversions_full

        except Exception as e:
            raise Exception('Loading custom unit failed!, ', e)

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

            # looping through all keys in _custom_conversions_full
            for key, custom_unit_dict in self._custom_conversions_full.items():

                # check
                if from_unit in custom_unit_dict and to_unit in custom_unit_dict:
                    return float(self.value) / float(custom_unit_dict[from_unit]) * float(custom_unit_dict[to_unit])

            raise ValueError("Custom conversion units not found")

            # check
            # if from_unit not in self._custom_conversions or to_unit not in self._custom_conversions:
            #     raise ValueError("Custom conversion units not found")

            # return float(self.value) / float(self._custom_conversions[from_unit]) * float(self._custom_conversions[to_unit])
        except Exception as e:
            raise Exception('Conversion failed!, ', e)
