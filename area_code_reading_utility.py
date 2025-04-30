import json

class AreaCodeReadingUtility:

    file_path = 'area_codes.json'

    def load_area_codes(self):
        with open(self.file_path, 'r', encoding='utf-8') as file:
            code_area_dict: dict[str,str] = {}
            data = json.load(file)
            for entry in data:
                area_number = str(entry['number'])
                area_name = str(entry['name'])
                code_area_dict[area_number] = area_name
        return code_area_dict
