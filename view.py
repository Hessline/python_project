import tkinter as tk
from tkinter import Listbox, Scrollbar, Entry, Button, Label, messagebox
from tkinter import filedialog
import controller

# GUI erstellen
root = tk.Tk()
root.title("Passwort Manager")


# Create a function to set a common width for buttons
def set_button_width(button):
    button.config(width=18)


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
login_listbox.bind("<<ListboxSelect>>", controller.display_login)

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
show_password_button = Button(frame_right, text="Anzeigen/Verbergen", command=controller.toggle_password_visibility)
show_password_button.pack(anchor='w', padx=0, pady=(5, 30))
set_button_width(show_password_button)

# Button "Hinzufügen"
add_button = Button(frame_right, text="Hinzufügen", command=controller.add_login)
add_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(add_button)

# Button "Löschen"
delete_button = Button(frame_right, text="Löschen", command=controller.delete_login)
delete_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(delete_button)

# Speichern-Button
save_button = Button(frame_right, text="Speichern", command=controller.save_login_data)
save_button.pack(anchor='w', padx=0, pady=(0, 15))
set_button_width(save_button)

# Import-Button erstellen
import_button = Button(frame_right, text="Importieren", command=controller.import_login_data)
import_button.pack(anchor='w', padx=0, pady=(0, 0))
set_button_width(import_button)
