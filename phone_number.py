from dataclasses import dataclass

@dataclass
class PhoneNumber:
    country_code: str
    area_code: str
    phone_number: str
    extension: str

