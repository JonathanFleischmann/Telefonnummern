from phone_info_extractor import PhoneInfoExtractor
from phone_number import PhoneNumber
from number_information import NumberInformation

from user_interface import UserInterface

test_strings = [
    "+49 0201 123456",
    "+44 0201123456",
    "0033 0201/123456",
    "0049201123456",
    "(0)201 1234 56",
    "+49 (941) 790-4780",
    "015115011900",
    "+91 09870987 899",
    "[+49] (0)89-800/849-50",
    "+49 (8024) [990-477]"
]

for test_string in test_strings:
    print(f"Test string: {test_string}")
    phone_info_extractor = PhoneInfoExtractor()
    try:
        phone_info: dict[PhoneNumber, NumberInformation] = phone_info_extractor.get_extracted_info_from_phone_number(test_string)
        print(f"Phone number: {phone_info[0].country_code}, {phone_info[0].area_code}, {phone_info[0].phone_number}, {phone_info[0].extension}")
    except ValueError as e:
        print(f"Error: {e}")
    
UserInterface().start_user_interface()