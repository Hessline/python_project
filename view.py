import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, Button, Label, messagebox
from tkinter import filedialog
import controller
from controller import generate_and_fill_password

# GUI erstellen
root = tk.Tk()
root.title("Passwort Manager")


# Create a function to set a common width for buttons
def set_button_width(button):
    button.config(width=18)


# Linke Seite (Login-Liste)
frame_left = tk.Frame(root)
frame_left.pack(side=tk.LEFT, padx=10, pady=10, anchor='n')
frame_left_label = tk.Label(frame_left, text="Gespeicherte Logins", font=("Helvetica", 14, "bold"))
frame_left_label.pack(side="top", anchor="w")
login_listbox = Listbox(frame_left, width=50, height=27)
login_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar = Scrollbar(frame_left, orient=tk.VERTICAL)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
login_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=login_listbox.yview)
login_listbox.bind("<<ListboxSelect>>", controller.display_login)

# Rechte Seite (Login-Daten)
frame_right = tk.Frame(root)
frame_right.pack(side=tk.RIGHT, padx=10, pady=10, expand=True, fill=tk.BOTH)

# Titel "Login-Daten"
frame_right_label = tk.Label(frame_right, text="Login-Daten", font=("Helvetica", 14, "bold"))
frame_right_label.pack(side="top", anchor="w", padx=0, pady=0)

# Label "Webseite"
website_label = Label(frame_right, text="Website:", font=("Helvetica", 10, "bold"))
website_label.pack(anchor='w', padx=0, pady=(20, 5))
website_entry = Entry(frame_right, width=50)
website_entry.pack(anchor='w')

# Label "Username"
username_label = Label(frame_right, text="Username:", font=("Helvetica", 10, "bold"))
username_label.pack(anchor='w', padx=0, pady=(20, 5))
username_entry = Entry(frame_right, width=50)
username_entry.pack(anchor='w')

# Label "Passwort"
password_label = Label(frame_right, text="Passwort:", font=("Helvetica", 10, "bold"))
password_label.pack(anchor='w', padx=0, pady=(20, 5))
password_entry = Entry(frame_right, show="*", width=50)
password_entry.pack(anchor='w')
password_visible = tk.IntVar()

# Button "Anzeigen/Verbergen" und "Random-Button" in einer eigenen Frame platzieren
button_frame = tk.Frame(frame_right)
button_frame.pack(anchor='w', padx=0, pady=(5, 25))

show_password_button = Button(button_frame, text="Anzeigen/Verbergen", command=controller.toggle_password_visibility)
show_password_button.pack(side="left", padx=0)
set_button_width(show_password_button)

random_button = Button(button_frame, text="Passwort generieren",
                       command=lambda: controller.generate_and_fill_password(password_entry))
random_button.pack(side="left", padx=5)
set_button_width(random_button)

# Button "Hinzufügen" und "Löschen" in einer eigenen Frame platzieren
ds_button_frame = tk.Frame(frame_right)
ds_button_frame.pack(anchor='w', padx=0, pady=(0, 25))

# Button "Hinzufügen"
add_button = Button(frame_right, text="Login Hinzufügen", command=controller.add_login)
add_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(add_button)

# Button "Löschen"
delete_button = Button(frame_right, text="Login Löschen", command=controller.delete_login)
delete_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(delete_button)

# Button "Speichern" und "Import" in einer eigenen Frame platzieren
file_button_frame = tk.Frame(frame_right)
file_button_frame.pack(anchor="w", padx=0, pady=(0, 15))

# Speichern-Button
save_button = Button(frame_right, text="File Speichern", command=controller.save_login_data)
save_button.pack(side="left", padx=0)
set_button_width(save_button)

# Import-Button erstellen
import_button = Button(frame_right, text="File Importieren", command=controller.import_login_data)
import_button.pack(side="left", padx=5)
set_button_width(import_button)
