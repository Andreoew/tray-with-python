import pystray
from PIL import Image, ImageDraw
from tkinter import filedialog
import tkinter as tk
import os

image = Image.open("sistema.png")

def on_clicked(icon, item):
    if str(item) == "Say Hello":
        print("Hello World")
    elif str(item) == "Usuário":
       print("Usuário")
    elif str(item) == "Submenu":
        file_path = get_file_path()
        print(f"Selected file: {file_path}")
    elif str(item) == "Subitem 1":
        print("Sub 1")
        file_path = get_file_path(initial_dir="/home/")
        print(f"Selected file: {file_path}")
    elif str(item) == "Subitem 2":
        print("Sub 2")
    elif str(item) == "Exit":
        icon.stop()

def get_file_path(initial_dir=None):
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=initial_dir)
    return file_path

menu = pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Usuário", on_clicked),   
    pystray.MenuItem("Submenu", pystray.Menu(
        pystray.MenuItem("Subitem 1", on_clicked),
        pystray.MenuItem("Subitem 2", on_clicked)
    )),
     pystray.MenuItem("Exit", on_clicked),
)

icon = pystray.Icon("Sistema", image, menu=menu)

icon.run()
