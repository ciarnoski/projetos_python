import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x600")


label_nome = tk.Label(root, text="digite seu nome:")
label_nome.pack(pady=10)
entrynome = tk.Entry(root)
entrynome.pack(pady=10)


labeldata = tk.Label(root, text="digite sua data de nascimento:")
labeldata.pack(pady=10)
entrydata = tk.Entry(root)
entrydata.pack(pady=10)


def info():
    nome = entrynome.get()
    data= entrydata.get()
    print(f"Nome: {nome}")
    print(f"Data de nascimento: {data}")
    resultado.config(text=f"Nome: {nome}, data de Nascimento: {data}")


botao_obter = tk.Button(root, text="obter informações", command=info)
botao_obter.pack(pady=10)


resultado = tk.Label(root, text="")
resultado.pack(pady=10)

root.mainloop()