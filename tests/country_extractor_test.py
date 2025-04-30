import pytest
from country_extractor import get_country_from_code

def test_get_country_from_code_possible_value():
    # Test with a known country code
    result = get_country_from_code("1")
    assert result == "United States"

def test_get_country_from_code_unknown_value():
    # Test with an unknown country code
    result = get_country_from_code("999")
    assert result == "Unknown country code"

def test_get_country_from_code_empty_value():
    # Test with an empty string, assert it returns a default value
    result = get_country_from_code("")
    assert result == "Germany"