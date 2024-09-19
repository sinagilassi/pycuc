# import packages/modules

# local
from .docs import CustomUnitConverter, Utils
from .config import __version__


def check_version():
    '''
    Check the version of the package

    Returns
    -------
    str
        The version of the package
    '''
    return __version__


def check_reference(reference: str, dataframe=True):
    '''
    Shows reference unit table

    Parameters
    ----------
    reference : str
        reference name such as pressure, temperature, custom

    Returns
    -------
    reference : dict | dataframe
        reference details

    Notes
    ------
    1. The reference can be set to 'PRESSURE', 'TEMPERATURE', 'CUSTOM'

    Examples
    --------
    >>> # ! pressure
    >>> print(pycuc.check_reference('pressure'))

    >>> # ! temperature
    >>> print(pycuc.check_reference('temperature'))

    >>> # ! custom
    >>> print(pycuc.check_reference('custom'))
    '''
    try:
        # check reference
        if isinstance(reference, str) and len(reference) > 0:
            cucC = CustomUnitConverter('', '')
            # check reference
            return cucC.check_reference(reference, dataframe)
        else:
            raise Exception('Reference not provided!')

    except Exception as e:
        raise Exception('Checking references failed!, ', e)


def create_cuc(value: float, unit: str) -> CustomUnitConverter:
    '''
    Define a CustomUnitConverter object

    Parameters
    ----------
    value : float
        The value to be converted
    unit : str
        The unit of the value

    Returns
    -------
    CustomUnitConverter
        A CustomUnitConverter object

    Examples
    --------
    >>> # ! pressure
    >>> my_cuc_1 = pycuc.create_cuc(1, 'MPa')
    >>> # convert to Pa
    >>> print(my_cuc_1.convert('Pa'))

    >>> print(my_cuc_1.convert('bar'))

    >>> print(my_cuc_1.convert('kPa'))
    >>>
    >>> # ! temperature
    >>> my_cuc_2 = pycuc.create_cuc(358, 'K')
    >>> # convert to K
    >>> print(my_cuc_2.convert('C'))

    >>> print(my_cuc_2.convert('F'))

    >>> print(my_cuc_2.convert('R'))
    >>>
    >>> # ! heat capacity unit: J/mol.K
    >>> my_cuc_3 = pycuc.create_cuc(25, 'J/mol.K')
    >>> # add custom
    >>> my_cuc_3.add_custom_unit('J/mol.K', 1)
    >>> my_cuc_3.add_custom_unit('kJ/mol.K', 1000)

    >>> # conversion
    >>> print(my_cuc_3.convert('J/mol.K'))
    >>> print(my_cuc_3.convert('kJ/mol.K'))

    '''
    return CustomUnitConverter(value, unit)


def convert_from_to(value: float, from_unit: str, to_unit: str, reference=None, reference_file=None) -> float:
    '''
    Convert a value from one unit to another

    Parameters
    ----------
    value : float
        The value to be converted
    from_unit : str
        The unit of the value
    to_unit : str
        The unit to convert to
    reference : str, optional
        The reference name such as 'PRESSURE', 'TEMPERATURE', 'CUSTOM'
    reference_file : str, optional
        The path to the reference file

    Returns
    -------
    float
        The converted value

    Notes
    ------
    1. The reference can be set to 'PRESSURE', 'TEMPERATURE', 'CUSTOM'
    2. If reference is None, then automatically set a value 

    Examples
    --------
    >>> # ! pressure
    >>> print(pycuc.convert_from_to(1, 'MPa', 'Pa'))
    >>> 
    >>> # ! temperature
    >>> print(pycuc.convert_from_to(358, 'K', 'C'))
    >>> print(pycuc.convert_from_to(25, 'C', 'K'))
    '''
    try:
        # custom object
        CustomUnitConverterC = CustomUnitConverter(value, from_unit)

        # conversion
        return CustomUnitConverterC.convert(to_unit, reference)

    except Exception as e:
        raise Exception('Conversion failed, ', e)


def to(value: float, unit_conversion_block: str, reference=None, reference_file=None) -> float:
    '''
    Convert a value from one unit to another using `unit conversion block`

    Parameters
    ----------
    value : float
        The value to be converted
    unit_conversion_block : str
        The block shows `(from_unit => to_unit)` such as (MPa => Pa), (K => C)
    reference : str, optional
        The reference name such as 'PRESSURE', 'TEMPERATURE', 'CUSTOM'
    reference_file : str, optional
        The reference file path

    Returns
    -------
    float
        The converted value

    Notes
    ------
    1. The reference can be set to 'PRESSURE', 'TEMPERATURE', 'CUSTOM'
    2. If reference is None, then automatically set a value

    Examples
    --------
    >>> # ! pressure
    >>> print(pycuc.to(1, 'MPa => Pa'))
    >>> 
    >>> # ! temperature
    >>> print(pycuc.to(358, 'K => C'))
    >>> print(pycuc.to(25, 'C => K'))
    '''
    try:
        # check conversion block
        from_unit, block_symbol, to_unit = Utils(
        ).parse_conversion_block(unit_conversion_block)

        return convert_from_to(value, from_unit, to_unit, reference)

    except Exception as e:
        raise Exception('Conversion failed, ', e)
