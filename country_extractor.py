from country_code_reading_utility import CountryCodeReadingUtility
from core import Core

class CountryExtractor:

    def __init__(self):
        self.code_country_dict = CountryCodeReadingUtility().load_country_codes()

    def get_country_and_remaining_number_from_phone_number(self, phone_number: str) -> tuple[str, str]:
        core = Core()

        country_code_prefix = ''

        cleaned_phone_number = core.clean_from_special_characters(phone_number)

        if cleaned_phone_number.startswith('+'): 
            country_code_prefix = '+'

        elif cleaned_phone_number.startswith('00'):
            country_code_prefix = '00'

        if country_code_prefix == '':
            if cleaned_phone_number.startswith('0'):
                return (self.code_country_dict.get(''), core.remove_prefix_until(phone_number, '0'))
            else:
                raise ValueError(f"Incorrect Phone Number Format - missing leading 0")
        
        if country_code_prefix == '+':
            remaining_phone_number = core.remove_prefix_until(phone_number, '+')
        else:
            remaining_phone_number = core.remove_prefix_until(phone_number, '00')

        remaining_phone_number = core.clean_from_special_characters(remaining_phone_number)

        for country_code in self.code_country_dict.keys():
            if remaining_phone_number.startswith(country_code):
                return (self.code_country_dict[country_code], core.remove_prefix_until(phone_number, country_code))

        raise ValueError(f"Incorrect Country Code")