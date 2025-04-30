import pytest
from phone_info_extractor import PhoneInfoExtractor
from phone_number import PhoneNumber
from number_information import NumberInformation

@pytest.fixture
def phone_info_extractor():
    return PhoneInfoExtractor()

def test_get_extracted_info_from_phone_number_happy_path(phone_info_extractor):
    # Test with a valid phone number
    phone_number = "+4930123456789"

    # Expected results
    expected_phone_number = PhoneNumber("+49", "30", "123456789", None)
    expected_number_info = NumberInformation("Germany", "Berlin")

    # Call the method
    result = phone_info_extractor.get_extracted_info_from_phone_number(phone_number)

    assert_results_equal(result, expected_phone_number, expected_number_info)

def test_get_extracted_info_with_extension(phone_info_extractor):
    # Test with a phone number that includes an extension
    phone_number = "+4930123456789-123"

    # Expected results
    expected_phone_number = PhoneNumber("+49", "30", "123456789", "123")
    expected_number_info = NumberInformation("Germany", "Berlin")

    # Call the method
    result = phone_info_extractor.get_extracted_info_from_phone_number(phone_number)

    assert_results_equal(result, expected_phone_number, expected_number_info)

def test_get_extracted_info_invalid_country_code(phone_info_extractor):
    # Test with an invalid country code
    phone_number = "+99 930123456789"

    with pytest.raises(ValueError, match="Incorrect Country Code"):
        result = phone_info_extractor.get_extracted_info_from_phone_number(phone_number)
        print(result)

def test_get_extracted_info_invalid_area_code(phone_info_extractor):
    # Test with an invalid area code
    phone_number = "+49123123456789"

    with pytest.raises(ValueError, match="Unknown Area Code"):
        phone_info_extractor.get_extracted_info_from_phone_number(phone_number)

def test_get_extracted_info_missing_country_code(phone_info_extractor):
    # Test with a phone number missing a country code
    phone_number = "30123456789"

    with pytest.raises(ValueError, match="Incorrect Phone Number Format - missing leading 0"):
        phone_info_extractor.get_extracted_info_from_phone_number(phone_number)

def test_get_extracted_info_empty_phone_number(phone_info_extractor):
    # Test with an empty phone number
    phone_number = ""

    with pytest.raises(ValueError, match="Incorrect Phone Number Format - missing leading 0"):
        phone_info_extractor.get_extracted_info_from_phone_number(phone_number)

def assert_results_equal(result, expected_phone_number, expected_number_info):
    assert result[0].country_code == expected_phone_number.country_code
    assert result[0].area_code == expected_phone_number.area_code
    assert result[0].phone_number == expected_phone_number.phone_number
    assert result[0].extension == expected_phone_number.extension

    assert result[1].country == expected_number_info.country
    assert result[1].area == expected_number_info.area