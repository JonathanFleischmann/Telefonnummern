import phonenumbers
from phonenumbers import geocoder, carrier, timezone


input_number = input("Enter a phone number: ")
input_number = ''.join(filter(str.isdigit, input_number))

parsed_number = phonenumbers.parse(input_number, "DE")

if phonenumbers.is_valid_number(parsed_number):
    print(f"The phone number {input_number} is valid.")
else:
    print(f"The phone number {input_number} is invalid.")
    exit()

print(f"Landesvorwahl: {parsed_number.country_code}")
print(f"Nationalnummer: {parsed_number.national_number}")
print(f"Region: {geocoder.description_for_number(parsed_number, "de")}")