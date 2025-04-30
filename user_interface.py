import tkinter as tk
from tkinter import messagebox


from phone_info_extractor import PhoneInfoExtractor
from phone_number import PhoneNumber
from number_information import NumberInformation


class UserInterface:

    def start_user_interface(self):
        global entry

        root = tk.Tk()
        root.title("Telefonnummernservice")
        root.geometry("300x200")

        label = tk.Label(root, text="Bitte geben Sie eine Telefonnummer ein:")
        label.pack(pady=20)

        entry = tk.Entry(root, width=30)
        entry.pack(pady=5)
        entry.focus()

        submit_button = tk.Button(root, text="Überprüfen", command=self.check_number)
        submit_button.pack(pady=10)

        exit_button = tk.Button(root, text="Beenden", command=root.quit)
        exit_button.pack(pady=5)

        root.mainloop()

    def check_number(self):
            phone_number = entry.get()
            if phone_number:
                phone_info_extractor = PhoneInfoExtractor()
                try:
                    phone_info: dict[PhoneNumber, NumberInformation] = phone_info_extractor.get_extracted_info_from_phone_number(phone_number)
                    output: str = f"Ihre eingegebene Telefonnummer: {phone_number}"
                    country: str = phone_info[1].country or 'unbekannt'
                    area_code: str = phone_info[1].area or 'unbekannt'
                    output += f"\nLand: {country}"
                    output += f"\nVorwahl: {area_code}"
                    messagebox.showinfo("Ergebnis", output)
                except ValueError as e:
                    messagebox.showerror("Fehler", f"Ungültige Telefonnummer: {e}")
            else:
                messagebox.showwarning("Eingabe", "Bitte geben Sie eine Telefonnummer ein.")
