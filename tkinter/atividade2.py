import tkinter as tk


root = tk.Tk()

cliques = 0
def contar():
    global cliques
    cliques += 1
    label.config(text=f"numero de cliques: {cliques}")
def zerar():
    global cliques
    cliques = 0
    label.config(text="Número de cliques: 0")

label = tk.Label(root, text="numero de cliques: 0")
label.pack(pady=20)

botaocontar= tk.Button(root, text="clique para somar", command=contar)
botaocontar.pack(pady=10)

botaozerar = tk.Button(root, text="zerar", command=zerar)
botaozerar.pack(pady=10)
root.mainloop()

