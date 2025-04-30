from dataclasses import dataclass
from phone_number import PhoneNumber

class DIN5008Formatter:
    @staticmethod
    def format_to_din5008(phone: PhoneNumber) -> str:
        """Formatiert ein PhoneNumber-Objekt in das DIN 5008-Format."""
        parts = []

        if phone.country_code:
            if phone.country_code.startswith("+"):
                parts.append(phone.country_code.strip())
            else:
                parts.append("+" + phone.country_code.strip())


        elif not phone.country_code and phone.area_code:
            parts.append("0" + phone.area_code.strip())  

        if phone.area_code:
            parts.append(phone.area_code.strip())
        elif not phone.area_code and not phone.country_code:
            parts.append("0" + phone.phone_number.strip())
        else:
            parts.append(phone.phone_number.strip())
        

        if phone.extension:
            return " ".join(parts) + f"-{phone.extension.strip()}"

        return " ".join(parts)
