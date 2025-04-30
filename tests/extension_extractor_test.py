import pytest
from extension_extractor import ExtensionExtractor

from phone_parse_result import PhoneParseResult

@pytest.fixture
def extension_extractor():
    return ExtensionExtractor()

def test_get_extension_valid(extension_extractor):
    # Test with a valid extension
    phone_number = "1234567-123"
    result = extension_extractor.get_extension_from_remaining_phone_number(phone_number)
    assert result == PhoneParseResult(None, "123", "1234567")

def test_get_extension_no_extension(extension_extractor):
    # Test with no valid extension (last sequence too long)
    phone_number = "1234567-12345"
    with pytest.raises(ValueError, match="No Extension Found"):
        extension_extractor.get_extension_from_remaining_phone_number(phone_number)


def test_get_extension_special_characters(extension_extractor):
    # Test with special characters in the phone number
    phone_number = "123-456/789-12"
    result = extension_extractor.get_extension_from_remaining_phone_number(phone_number)
    assert result == ("12", "123-456/789")