from dataclasses import dataclass
from phone_number import PhoneNumber

class DIN5008Formatter:
    @staticmethod
    def format_to_din5008(phone: PhoneNumber) -> str:
        """Formatiert ein PhoneNumber-Objekt in das DIN 5008-Format."""
        parts = []
        # Landesvorwahl (falls vorhanden)
        if phone.country_code:
            parts.append(phone.country_code.strip())
        else:
            parts.append("0")  # Standard für nationale Nummern

        # Ortskennzahl (falls vorhanden)
        if phone.area_code:
            parts.append(phone.area_code.strip())

        # Telefonnummer (Pflichtfeld)
        parts.append(phone.phone_number.strip())

        # Durchwahl (falls vorhanden)
        if phone.extension:
            parts.append(phone.extension.strip())

        # Verbinden der Teile mit Leerzeichen
        return " ".join(parts)
