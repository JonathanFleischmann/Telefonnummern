from phone_info_extractor import PhoneInfoExtractor
from phone_number import PhoneNumber
from number_information import NumberInformation
from phone_number_formatter import DIN5008Formatter

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
    phone_info_extractor = PhoneInfoExtractor()
    din_5008_formatter = DIN5008Formatter()
    try:
        phone_number_obj, _  = phone_info_extractor.get_extracted_info_from_phone_number(test_string)
        print(phone_number_obj)
        formatted_number = din_5008_formatter.format_to_din5008(phone_number_obj)
        print(f"Original: {test_string} => Formatted: {formatted_number}")
    except ValueError as e:
        print(f"Error: {e}")
