from country_code_reading_utility import load_country_codes

code_country_dict = load_country_codes()

def get_country_from_code(code: str) -> str:
    return country_codes.get(code, "Unknown country code")