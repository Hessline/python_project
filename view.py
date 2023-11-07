import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, Button, Label, messagebox
from tkinter import filedialog

#Login-Daten Array
login_data = []

def display_login(event):
    selected_indices = login_listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        login = login_data[index]
        website_entry.delete(0, tk.END)
        website_entry.insert(0, login["Website"])
        username_entry.delete(0, tk.END)
        username_entry.insert(0, login["Username"])
        password_entry.delete(0, tk.END)
        password_entry.insert(0, login["Password"])
    else:
        # Zeige eine Meldung oder führe eine andere Aktion aus, wenn keine Elemente ausgewählt wurden
        pass

#Create a function to set a common width for buttons
def set_button_width(button):
    button.config(width=18)

def add_login():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if not website or not username or not password:
        messagebox.showerror("Fehler", "Bitte fülle alle Felder aus.")
    else:
        login_data.append({"Website": website, "Username": username, "Password": password})
        login_listbox.insert(tk.END, website)

def delete_login():
    try:
        index = login_listbox.curselection()[0]
        login_to_delete = login_data[index]

        confirm = messagebox.askokcancel("Bestätigung",
                                         f"Möchtest du den Login für {login_to_delete['Website']} wirklich löschen?")

        if confirm:
            login_listbox.delete(index)
            del login_data[index]
            clear_entries()
    except IndexError:
        messagebox.showerror("Fehler", "Bitte wähle einen Eintrag zum Löschen aus.")

def clear_entries():
    website_entry.delete(0, tk.END)
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

def toggle_password_visibility():
    current_password = password_entry.get()
    password_entry.delete(0, tk.END)
    if password_visible.get() == 1:
        password_entry.config(show="*")
        password_visible.set(0)
    else:
        password_entry.config(show="")
        password_visible.set(1)
    password_entry.insert(0, current_password)

def save_login_data():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Dateien", "*.txt")])

    if file_path:
        with open(file_path, "w") as file:
            for login in login_data:
                file.write(f"Website: {login['Website']}\n")
                file.write(f"Username: {login['Username']}\n")
                file.write(f"Password: {login['Password']}\n")
                file.write("\n")

def import_login_data():
    file_path = filedialog.askopenfilename(filetypes=[("Text Dateien", "*.txt")])

    if file_path:
        with open(file_path, "r") as file:
            imported_data = file.read()

# GUI erstellen
root = tk.Tk()
root.title("Passwort Manager")

# Linke Seite (Login-Liste)
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10)
frame_left_label = tk.Label(frame_left, text="Gespeicherte Logins", font=("Helvetica", 14, "bold"))
frame_left_label.pack(side="top", anchor="w")
login_listbox = Listbox(frame_left, width=50, height=30)
login_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = Scrollbar(frame_left, orient=tk.VERTICAL)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
login_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=login_listbox.yview)
login_listbox.bind("<<ListboxSelect>>", display_login)

# Rechte Seite (Login-Daten)
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10, anchor='n')

# Titel "Login-Daten"
frame_right_label = tk.Label(frame_right, text="Login-Daten", font=("Helvetica", 14, "bold"))
frame_right_label.pack(side="top", anchor="w", padx=0, pady=0)

# Label "Webseite"
website_label = Label(frame_right, text="Website:", font=("Helvetica", 10, "bold"))
website_label.pack(anchor='w', padx=0, pady=(20, 5))
website_entry = Entry(frame_right, width=50)
website_entry.pack()

# Label "Username"
username_label = Label(frame_right, text="Username:", font=("Helvetica", 10, "bold"))
username_label.pack(anchor='w', padx=0, pady=(20, 5))
username_entry = Entry(frame_right, width=50)
username_entry.pack()

# Label "Passwort"
password_label = Label(frame_right, text="Passwort:", font=("Helvetica", 10, "bold"))
password_label.pack(anchor='w', padx=0, pady=(20, 5))
password_entry = Entry(frame_right, show="*", width=50)
password_entry.pack()
password_visible = tk.IntVar()

# Button "Anzeigen/Verbergen"
show_password_button = Button(frame_right, text="Anzeigen/Verbergen", command=toggle_password_visibility)
show_password_button.pack(anchor='w', padx=0, pady=(5, 30))
set_button_width(show_password_button)

# Button "Hinzufügen"
add_button = Button(frame_right, text="Hinzufügen", command=add_login)
add_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(add_button)

# Button "Löschen"
delete_button = Button(frame_right, text="Löschen", command=delete_login)
delete_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(delete_button)

# Speichern-Button
save_button = Button(frame_right, text="Speichern", command=save_login_data)
save_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(save_button)

# Import-Button erstellen
import_button = Button(frame_right, text="Importieren", command=import_login_data)
import_button.pack(anchor='w', padx=0, pady=(0, 0))
set_button_width(import_button)

# Initialisiere die Login-Liste
for login in login_data:
    login_listbox.insert(tk.END, login["Website"])

root.mainloop()
