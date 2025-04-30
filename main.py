from country_extractor import CountryExtractor
from area_extractor import AreaExtractor


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
    country_extractor = CountryExtractor()
    area_extractor = AreaExtractor()
    try:
        country_result: tuple[str, str]  = country_extractor.get_country_and_remaining_number_from_phone_number(test_string)
        if country_result[0] == "Germany":
            area_result: tuple[str, str] = area_extractor.get_area_and_remaining_number_from_remaining_phone_number(country_result[1])
            print(f"Result: {country_result[0]} {area_result[0]} {area_result[1]}")#
        else:
            print(f"Result: {country_result[0]} {country_result[1]}")
    except ValueError as e:
        # catch the ValueError and print the error message
        print(f"Error: {e}")
