# import module/packages
import re
import os
import yaml


class Utils:

    def __init__(self):
        pass

    def parse_conversion_block(self, input_str):
        '''
        Checks conversion string

        Parameters
        ----------
        input_str : str
            conversion string

        Returns
        -------
        subgroups : list
            list of subgroups
        '''
        try:
            # remove space
            input_str = input_str.strip()

            # Regular expression pattern with '=>' as a required part
            pattern = r"(.*)\s*=>\s*(.*)"

            # Find matches
            match = re.match(pattern, input_str)

            if match:
                # Get subgroups and strip leading/trailing whitespace
                subgroups = [match.group(1).strip(),
                             '=>', match.group(2).strip()]
                return subgroups
            else:
                raise ValueError("Input string does not contain '=>'")
        except Exception as e:
            raise Exception('Parsing conversion failed!, ', e)

    def _load_custom_conversion_unit(self, f):
        '''
        Load custom conversion unit

        Parameters
        ----------
        f : str
            yml file path

        Returns
        -------
        dict
            custom conversion unit
        '''
        try:
            # custom unit
            custom_unit = {}

            # check file path
            if not os.path.exists(f):
                raise ValueError("File not found")

            # check format
            if not f.endswith('.yml'):
                raise ValueError("File format not supported")

            # read yml file
            with open(f, 'r') as file:
                custom_unit = yaml.safe_load(file)

            return custom_unit

        except Exception as e:
            raise Exception('Loading custom conversion unit failed!, ', e)
