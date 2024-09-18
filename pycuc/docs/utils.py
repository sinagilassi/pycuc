# import module/packages
import re


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
