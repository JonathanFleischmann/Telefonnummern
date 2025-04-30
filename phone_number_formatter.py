from dataclasses import dataclass
from phone_number import PhoneNumber

class DIN5008Formatter:
    @staticmethod
    def format_to_din5008(phone: PhoneNumber) -> str:
        """Formatiert ein PhoneNumber-Objekt in das DIN 5008-Format."""
        parts = []
        number_stripped = False

     # 1. Landesvorwahl
        if phone.country_code:
            # Füge die Landesvorwahl hinzu, stelle sicher, dass sie mit "+" beginnt
            if phone.country_code.startswith("+"):
                parts.append(phone.country_code.strip())
            else:
                parts.append("+" + phone.country_code.strip())

        # 2. Ortskennzahl
        if phone.area_code:
            # Füge die Ortskennzahl hinzu, nur wenn sie existiert
            parts.append(phone.area_code.strip())
        elif not phone.country_code and phone.phone_number:
            # Wenn keine Landesvorwahl vorhanden ist, aber Telefonnummer existiert, füge "0" hinzu
            parts.append("0" + phone.phone_number.strip())
            number_stripped = True

        # 3. Telefonnummer
        if phone.phone_number and not number_stripped:
            # Füge die Telefonnummer hinzu, wenn sie existiert
            parts.append(phone.phone_number.strip())
            number_stripped = False

        # 4. Durchwahl
        if phone.extension:
            # Füge die Durchwahl hinzu, falls vorhanden
            return " ".join(parts) + f"-{phone.extension.strip()}"

        # Rückgabe ohne Durchwahl
        return " ".join(parts)
