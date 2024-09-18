# import packages/modules

# local
from .docs import CustomUnitConverter
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


def convert_from_to(value: float, from_unit: str, to_unit: str, reference=None) -> float:
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
