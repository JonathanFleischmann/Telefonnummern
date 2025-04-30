from country_code_reading_utility import load_country_codes

code_country_dict = load_country_codes()

def get_country_from_code(code: str) -> str:
    return code_country_dict.get(code, "Unknown country code")