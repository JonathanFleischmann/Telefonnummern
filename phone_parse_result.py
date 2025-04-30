from dataclasses import dataclass

@dataclass
class PhoneParseResult:
    value: str
    code: str
    remaining_number: str