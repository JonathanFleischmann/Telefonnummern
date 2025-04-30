import pytest
from area_extractor import AreaExtractor

@pytest.fixture
def area_extractor():
    # Mock the AreaExtractor with sample area codes for testing
    extractor = AreaExtractor()
    extractor.code_area_dict = {
        "30": "Berlin",
        "40": "Hamburg",
        "89": "Munich"
    }
    return extractor

def test_valid_area_code(area_extractor):
    # Test with a valid area code
    result = area_extractor.get_area_and_remaining_number_from_remaining_phone_number("30 1234567")
    assert result == ("Berlin", "1234567")

def test_valid_area_code_with_special_characters(area_extractor):
    # Test with a valid area code and special characters
    result = area_extractor.get_area_and_remaining_number_from_remaining_phone_number("(40) 9876543")
    assert result == ("Hamburg", "9876543")

def test_unknown_area_code(area_extractor):
    # Test with an unknown area code
    with pytest.raises(ValueError, match="Unknown Area Code"):
        area_extractor.get_area_and_remaining_number_from_remaining_phone_number("99 1234567")

def test_empty_phone_number(area_extractor):
    # Test with an empty phone number
    with pytest.raises(ValueError, match="Unknown Area Code"):
        area_extractor.get_area_and_remaining_number_from_remaining_phone_number("")