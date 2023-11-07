import tkinter as tk
from model import Model
from view import View
from controller import Controller

def main():
    root = tk.Tk()
    root.title("Password Manager")

    model = Model()
    controller = Controller(model, view)
    view = View(root, controller)
    controller.view = view

    root.mainloop()

if __name__ ==  "__main__":
    main()

