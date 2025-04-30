import pytest
from core import Core

@pytest.fixture
def core():
    return Core()

def test_remove_prefix_until_valid_prefix(core):
    # Test with a valid prefix
    result = core.remove_prefix_until("00123456789", "00")
    assert result == "123456789"

def test_remove_prefix_until_prefix_not_found(core):
    # Test with a prefix that doesn't exist in the string
    with pytest.raises(ValueError, match="Prefix '99' not found in string."):
        core.remove_prefix_until("00123456789", "99")

def test_remove_prefix_until_empty_string(core):
    # Test with an empty string
    with pytest.raises(ValueError, match="Prefix '00' not found in string."):
        core.remove_prefix_until("", "00")

def test_clean_from_special_characters(core):
    # Test cleaning a string with special characters
    result = core.clean_from_special_characters("(123) [456]/789")
    assert result == "123456789"

def test_clean_from_special_characters_no_special_characters(core):
    # Test cleaning a string with no special characters
    result = core.clean_from_special_characters("123456789")
    assert result == "123456789"

def test_clean_from_special_characters_empty_string(core):
    # Test cleaning an empty string
    result = core.clean_from_special_characters("")
    assert result == ""