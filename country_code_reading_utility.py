import json

file_path = 'country_codes.json'


def load_country_codes():
    with open(file_path, 'r', encoding='utf-8') as file:
        code_country_dict: dict[str,str] = {}
        data = json.load(file)
        for entry in data:
            country_code = str(entry['code'])
            country_name = str(entry['country'])
            code_country_dict[country_code] = country_name
    return code_country_dict
