import pytest
from country_extractor import CountryExtractor

from phone_parse_result import PhoneParseResult

@pytest.fixture
def country_extractor():
    # Mock the CountryExtractor with sample country codes for testing
    extractor = CountryExtractor()
    extractor.code_country_dict = {
        "49": "Germany",
        "1": "United States",
        "44": "United Kingdom"
    }
    return extractor

def test_get_country_and_remaining_number_possible_value(country_extractor):
    # Test with a known country code
    result = country_extractor.get_country("+49123456789")
    assert result == PhoneParseResult("Germany",'49', "123456789")

def test_get_country_and_remaining_number_Britian(country_extractor):
    # Test with a known country code
    result = country_extractor.get_country("+44123456789")
    assert result == PhoneParseResult("United Kingdom",'44', "123456789")

def test_get_country_and_remaining_number_unknown_value(country_extractor):
    # Test with an unknown country code
    with pytest.raises(ValueError, match="Incorrect Country Code"):
        country_extractor.get_country("+999123456789")

def test_get_country_and_remaining_number_empty_value(country_extractor):
    # Test with an empty string, assert it raises an error
    with pytest.raises(ValueError, match="Incorrect Phone Number Format - missing leading 0"):
        country_extractor.get_country("")