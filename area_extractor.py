from area_code_reading_utility import AreaCodeReadingUtility
from core import Core

class AreaExtractor:

    def __init__(self):
        self.code_area_dict = AreaCodeReadingUtility().load_area_codes()

    def get_area_and_remaining_number_from_remaining_phone_number(self, remaining_phone_number: str) -> tuple[str, str, str]:

        filtered_phone_number = remaining_phone_number.replace(' ', '').replace('/', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '')
        
        area_code = ''

        for possible_area_code in self.code_area_dict.keys():
            if filtered_phone_number.startswith(possible_area_code):
                area_code = possible_area_code
                break

        if area_code == '':
            raise ValueError(f"Unknown Area Code")
        
        phone_number_without_area_code = Core().remove_prefix_until(remaining_phone_number, area_code)

        while phone_number_without_area_code and not phone_number_without_area_code[0].isdigit():
            phone_number_without_area_code = phone_number_without_area_code[1:]
                
        return (self.code_area_dict[area_code], area_code, phone_number_without_area_code)