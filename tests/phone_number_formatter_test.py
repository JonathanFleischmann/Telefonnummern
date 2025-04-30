import pytest
from phone_number_formatter import DIN5008Formatter
from phone_number import PhoneNumber

def test_format_to_din5008_with_country_code():
    # Test formatting with a country code
    phone = PhoneNumber(country_code="+49", area_code="30", phone_number="1234567", extension=None)
    result = DIN5008Formatter.format_to_din5008(phone)
    assert result == "+49 30 1234567"

def test_format_to_din5008_with_country_code_and_extension():
    # Test formatting with a country code and an extension
    phone = PhoneNumber(country_code="+49", area_code="30", phone_number="1234567", extension="89")
    result = DIN5008Formatter.format_to_din5008(phone)
    assert result == "+49 30 1234567-89"

def test_format_to_din5008_without_area_code():
    # Test formatting without an area code
    phone = PhoneNumber(country_code="+49", area_code=None, phone_number="1234567", extension=None)
    result = DIN5008Formatter.format_to_din5008(phone)
    assert result == "+49 1234567"

def test_format_to_din5008_without_area_code_and_with_extension():
    # Test formatting without an area code but with an extension
    phone = PhoneNumber(country_code="+49", area_code=None, phone_number="1234567", extension="89")
    result = DIN5008Formatter.format_to_din5008(phone)
    assert result == "+49 1234567-89"

def test_format_to_din5008_with_only_phone_number():
    # Test formatting with only a phone number
    phone = PhoneNumber(country_code=None, area_code=None, phone_number="1234567", extension=None)
    result = DIN5008Formatter.format_to_din5008(phone)
    assert result == "01234567"

def test_format_to_din5008_with_only_phone_number_and_extension():
    # Test formatting with only a phone number and an extension
    phone = PhoneNumber(country_code=None, area_code=None, phone_number="1234567", extension="89")
    result = DIN5008Formatter.format_to_din5008(phone)
    assert result == "01234567-89"