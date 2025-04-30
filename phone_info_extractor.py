from phone_number import PhoneNumber
from number_information import NumberInformation

from core import Core

from country_extractor import CountryExtractor
from area_extractor import AreaExtractor
from extension_extractor import ExtensionExtractor

class PhoneInfoExtractor:

    def get_extracted_info_from_phone_number(self, phone_number: str) -> dict[PhoneNumber, NumberInformation]:
        """
        Extracts country, area, and extension information from a given phone number.
        """
        country: str = None
        area: str = None

        country_code: str = None
        area_code: str = None
        number: str = None
        extension: str = None

        country_extractor = CountryExtractor()
        area_extractor = AreaExtractor()
        extension_extractor = ExtensionExtractor()

        core = Core()

        country_info = country_extractor.get_country_and_remaining_number_from_phone_number(phone_number)
        country = country_info[0]
        country_code = country_info[1]

        remaining_number = country_info[2]

        try:
            area_info = area_extractor.get_area_and_remaining_number_from_remaining_phone_number(remaining_number)
            area = area_info[0]
            area_code = area_info[1]

            remaining_number = area_info[2]

        except ValueError:
            area = None
            area_code = None

        try:
            extension_info = extension_extractor.get_extension_from_remaining_phone_number(remaining_number)
            extension = extension_info[0]
            number = core.clean_from_special_characters(extension_info[1])
            
        except ValueError:
            extension = None
            number = core.clean_from_special_characters(remaining_number)

        phone_number_obj = PhoneNumber(country_code, area_code, number, extension)
        number_info_obj = NumberInformation(country, area)

        return (phone_number_obj, number_info_obj)


