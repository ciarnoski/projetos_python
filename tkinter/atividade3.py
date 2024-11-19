import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("Minha Primeira GUI")
root.geometry("400x500")
label = tk.Label(root, text="Olá, Tkinter!")
label.pack(anchor= 'e', pady=10)
def on_button_click():
    print("Botão clicado!")
    label.config(text="Você clicou no botão!")
button = tk.Button(root, text="Clique em mim", command=on_button_click)
button.pack(anchor= 'e',pady=10)

entry = tk.Entry(root,  )
entry.pack(anchor= 'e', pady=10)

root.mainloop()