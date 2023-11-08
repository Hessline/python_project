import random
import string
from cryptography.fernet import Fernet


def generate_random_password(length):
    return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


class Model:
    login_data = []

    def add_password_details(self, website, username, password):
        self.login_data.append({"Website": website, "Username": username, "Password": password})

    def delete_password_details(self, index):
        self.login_data.pop(index)

    # Funktion zum Verschlüsseln von Daten und Speichern in einer Datei
    def encrypt_and_save_data(data, file_path):
        encrypted_data = cipher_suite.encrypt(data.encode())
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

    # Funktion zum Lesen und Entschlüsseln von Daten aus einer Datei
    def load_and_decrypt_data(file_path):
        try:
            with open(file_path, "rb") as file:
                encrypted_data = file.read()
                decrypted_data = cipher_suite.decrypt(encrypted_data)
                return decrypted_data.decode()
        except Exception as e:
            messagebox.showerror("Fehler", "Fehler beim Lesen oder Entschlüsseln der Datei: " + str(e))
