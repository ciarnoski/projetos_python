
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

def criar_label():  
    label = tk.Label(root, text="voce apertou nu butao:")
    label.pack(pady= 10)


botao = tk.Button(root, text = 'Aperte nu butão', command= criar_label)
botao.pack(pady= 20)

root.mainloop()



botao = tk.Button(root, text = 'Aperte nu butão', command= criar_label)
botao.pack(pady= 20)

root.mainloop()
