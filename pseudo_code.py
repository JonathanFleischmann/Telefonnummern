import re


class TelefonParser:
    def __init__(self, laender_vorwahlen=None):
        # Optional: Eine Datenbank mit Ländervorwahlen und Ortskennzahlinformationen
        self.laender_vorwahlen = laender_vorwahlen if laender_vorwahlen else {}

    @staticmethod
    def entferne_nicht_ziffern(text):
        """
        Entfernt alle Zeichen außer Ziffern.
        """
        return re.sub(r"[^\d]", "", text)

    @staticmethod
    def ist_ziffer(zeichen):
        """
        Prüft, ob das Zeichen eine Ziffer ist.
        """
        return zeichen.isdigit()

    @staticmethod
    def ist_alles_ziffern(text):
        """
        Prüft, ob der gesamte Text nur aus Ziffern besteht.
        """
        return text.isdigit()

    def parse_telefonnummer(self, eingabe_nummer):
        """
        Zerlegt eine Telefonnummer in Landesvorwahl, Ortskennzahl, Hauptnummer und Durchwahl.
        """
        # 1. Entferne alle nicht-ziffern-Zeichen
        bereinigte_nummer = self.entferne_nicht_ziffern(eingabe_nummer)
        landesvorwahl, ortskennzahl, nummer, durchwahl = "", "", "", ""

        # 2. Identifiziere die Landesvorwahl
        restliche_nummer = bereinigte_nummer
        if bereinigte_nummer.startswith("00"):
            landesvorwahl = bereinigte_nummer[:4]  # Annahme: Ländervorwahl ist max. 4 Stellen nach "00"
            restliche_nummer = bereinigte_nummer[4:]
        elif bereinigte_nummer.startswith("+"):
            landesvorwahl_länge = 1
            for i in range(1, min(4, len(bereinigte_nummer))):
                if self.ist_ziffer(bereinigte_nummer[i]):
                    landesvorwahl_länge = i + 1
                else:
                    break
            landesvorwahl = bereinigte_nummer[:landesvorwahl_länge]
            restliche_nummer = bereinigte_nummer[landesvorwahl_länge:]

        # 3. Identifiziere die Durchwahl
        if '-' in restliche_nummer:
            teile = restliche_nummer.split('-')
            nummer_potentiell = teile[0]
            durchwahl_potentiell = teile[-1]
            if len(durchwahl_potentiell) <= 5 and self.ist_alles_ziffern(durchwahl_potentiell):
                durchwahl = durchwahl_potentiell
                nummer = nummer_potentiell
            else:
                nummer = restliche_nummer
        else:
            nummer = restliche_nummer

        # 4. Extrahiere die Ortskennzahl (Beispielhaft für Deutschland)
        if landesvorwahl in ["49", "0049", "+49"]:
            if nummer.startswith("0"):
                # Suche nach der möglichen Ortskennzahl-Länge
                ortskennzahl_länge = 1
                while ortskennzahl_länge < len(nummer) - 4 and self.ist_ziffer(nummer[ortskennzahl_länge]):
                    ortskennzahl_länge += 1
                ortskennzahl = nummer[:ortskennzahl_länge]
                nummer = nummer[ortskennzahl_länge:]

        return {
            "landesvorwahl": landesvorwahl,
            "ortskennzahl": ortskennzahl,
            "nummer": nummer,
            "durchwahl": durchwahl,
        }

    def parse_mit_datenbank(self, eingabe_nummer):
        """
        Erweiterte Version mit Nutzung einer Ländervorwahldatenbank.
        """
        result = self.parse_telefonnummer(eingabe_nummer)
        landesvorwahl = result["landesvorwahl"]
        nummer_ohne_durchwahl = result["nummer"]

        if landesvorwahl in self.laender_vorwahlen:
            laender_info = self.laender_vorwahlen[landesvorwahl]
            typische_ortskennzahlen = laender_info.get("ortskennzahl_längen", [])
            for länge in typische_ortskennzahlen:
                if len(nummer_ohne_durchwahl) > länge:
                    ortskennzahl = nummer_ohne_durchwahl[:länge]
                    nummer = nummer_ohne_durchwahl[länge:]
                    result["ortskennzahl"] = ortskennzahl
                    result["nummer"] = nummer
                    break
        return result


# Beispielanwendung
parser = TelefonParser()
telefonnummer = "+49 30 1234567-89"
ergebnis = parser.parse_telefonnummer(telefonnummer)
print(ergebnis)
