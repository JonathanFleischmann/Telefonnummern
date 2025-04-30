from dataclasses import dataclass

@dataclass
class PhoneNumber:
    country_code: int
    prefix: int
    area_code: int
    phone_number: int
    extension: int

