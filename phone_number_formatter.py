import re

class PhoneNumberFormatter:
    def __init__(self, default_country_code="DE"):
        self.default_country_code = default_country_code

    def parse_phone_number(self, phone_number):
        """
        Zerlegt die Telefonnummer in Landesvorwahl, Ortskennzahl, Nummer und Durchwahl.
        """
        pattern = r"^(\+\d{1,3})?\s*\(?\d{2,4}\)?[\s.-]?\d{3,10}([\s.-]\d{1,5})?$"
        match = re.match(pattern, phone_number)
        if not match:
            raise ValueError("Ungültiges Telefonnummernformat")

        # Extrahieren der Bestandteile
        country_code = match.group(1) or f"+{self.get_country_code_from_iso(self.default_country_code)}"
        remaining_number = phone_number[len(country_code):].strip()
        
        # Ortskennzahl, Nummer und Durchwahl extrahieren
        local_parts = re.split(r"[\s.-]", remaining_number)
        if len(local_parts) < 2:
            raise ValueError("Unvollständige Telefonnummer")

        area_code = local_parts[0]
        main_number = local_parts[1]
        extension = local_parts[2] if len(local_parts) > 2 else None

        return {
            "country_code": country_code,
            "area_code": area_code,
            "main_number": main_number,
            "extension": extension,
        }

    def format_phone_number(self, components):
        """
        Formatiert die Telefonnummer in ein konsistentes Format.
        """
        formatted = f"{components['country_code']} {components['area_code']} {components['main_number']}"
        if components.get("extension"):
            formatted += f"-{components['extension']}"
        return formatted

    def validate_phone_number(self, phone_number):
        """
        Führt eine grundlegende Validierung der Telefonnummer durch.
        """
        pattern = r"^(\+\d{1,3})?\s*\(?\d{2,4}\)?[\s.-]?\d{3,10}([\s.-]\d{1,5})?$"
        return re.match(pattern, phone_number) is not None

    def store_in_database(self, components):
        """
        Simuliert das Speichern der Telefonnummer in einer Datenbank.
        """
        database_entry = {
            "country_code": components["country_code"],
            "area_code": components["area_code"],
            "main_number": components["main_number"],
            "extension": components.get("extension"),
        }
        return database_entry

    def get_country_code_from_iso(self, iso_code):
        """
        Gibt die Landesvorwahl basierend auf einem ISO-Ländercode zurück.
        """
        country_codes = {
            "DE": "49",
            "US": "1",
            "FR": "33",
            # Weitere Codes können hinzugefügt werden
        }
        return country_codes.get(iso_code, "49")

# Beispielhafte Verwendung
def main():
    formatter = PhoneNumberFormatter()
    phone_number = "+49 30 1234567-89"

    if formatter.validate_phone_number(phone_number):
        components = formatter.parse_phone_number(phone_number)
        formatted_number = formatter.format_phone_number(components)
        print("Formatiert:", formatted_number)

        database_entry = formatter.store_in_database(components)
        print("Datenbankeintrag:", database_entry)
    else:
        print("Ungültige Telefonnummer")

if __name__ == "__main__":
    main()
