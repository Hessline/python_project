from tkinter import filedialog

import view
from model import Model
from model import generate_random_password

model = Model()


def display_login(event):
    selected_indices = view.login_listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        login = model.login_data[index]
        view.website_entry.delete(0, view.tk.END)
        view.website_entry.insert(0, login["Website"])
        view.username_entry.delete(0, view.tk.END)
        view.username_entry.insert(0, login["Username"])
        view.password_entry.delete(0, view.tk.END)
        view.password_entry.insert(0, login["Password"])
    else:
        # Zeige eine Meldung oder führe eine andere Aktion aus, wenn keine Elemente ausgewählt wurden
        pass


def add_login():
    website = view.website_entry.get()
    username = view.username_entry.get()
    password = view.password_entry.get()
    if not website or not username or not password:
        view.messagebox.showerror("Fehler", "Bitte fülle alle Felder aus.")
    else:
        model.add_password_details(website, username, password)
        view.login_listbox.insert(view.tk.END, website)


def delete_login():
    try:
        index = view.login_listbox.curselection()[0]
        login_to_delete = model.login_data[index]

        confirm = view.messagebox.askokcancel("Bestätigung",
                                              f"Möchtest du den Login für {login_to_delete['Website']} wirklich löschen?")

        if confirm:
            view.login_listbox.delete(index)
            model.delete_password_details(index)
            clear_entries()
    except IndexError:
        view.messagebox.showerror("Fehler", "Bitte wähle einen Eintrag zum Löschen aus.")


def clear_entries():
    view.website_entry.delete(0, view.tk.END)
    view.username_entry.delete(0, view.tk.END)
    view.password_entry.delete(0, view.tk.END)


def toggle_password_visibility():
    current_password = view.password_entry.get()
    view.password_entry.delete(0, view.tk.END)
    if view.password_visible.get() == 1:
        view.password_entry.config(show="*")
        view.password_visible.set(0)
    else:
        view.password_entry.config(show="")
        view.password_visible.set(1)
    view.password_entry.insert(0, current_password)


def save_login_data():
    file_path = view.filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Dateien", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            for login in model.login_data:
                file.write(f"Website: {login['Website']}\n")
                file.write(f"Username: {login['Username']}\n")
                file.write(f"Password: {login['Password']}\n")
                file.write("\n")


def import_login_data():
    file_path = view.filedialog.askopenfilename(filetypes=[("Text Dateien", "*.txt")])

    if file_path:
        with open(file_path, "r") as file:
            imported_data = file.read()


# Initialisiere die Login-Liste
for login in model.login_data:
    view.login_listbox.insert(view.tk.END, login["Website"])


def generate_random_login():
    return None


def generate_and_fill_password(password_entry):
    password = generate_random_password(20)  # Ändere die Länge nach Bedarf
    password_entry.delete(0, view.tk.END)  # Lösche den aktuellen Inhalt des Eingabefelds
    password_entry.insert(0, password)


# Speichern-Button
def save_login_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".enc", filetypes=[("Verschlüsselte Dateien", "*.enc")])

    if file_path:
        data_to_save = "Website: {}\nUsername: {}\nPassword: {}\n".format(view.website_entry.get(), view.username_entry.get(),
                                                                          view.password_entry.get())
        model.encrypt_and_save_data(data_to_save, file_path)


# Import-Button
def import_login_data():
    file_path = filedialog.askopenfilename(filetypes=[("Verschlüsselte Dateien", "*.enc")])

    if file_path:
        decrypted_data = model.load_and_decrypt_data(file_path)
        if decrypted_data:
    # Verarbeiten Sie die entschlüsselten Daten, um Website, Benutzername und Passwort anzuzeigen oder zu speichern.
