from core import Core

class ExtensionExtractor:

    def __init__(self):
        pass
    
    def get_extension_from_remaining_phone_number(self, phone_number: str) -> tuple[str, str]:

        last_number_sequence = Core().get_last_number_sequence(phone_number)

        if len(last_number_sequence) > 3:
            raise ValueError(f"No Extension Found")
        
        remaining_phone_number = Core().remove_suffix_until(phone_number, last_number_sequence)

        while remaining_phone_number and not remaining_phone_number[-1].isdigit():
            remaining_phone_number = remaining_phone_number[:-1]
        
        return (last_number_sequence, remaining_phone_number)
