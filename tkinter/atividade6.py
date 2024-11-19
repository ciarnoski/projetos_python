import tkinter as tk

root = tk.Tk()


contador = 0

def criar_label():
    global contador
    contador += 1 
    label = tk.Label(root, text=f"Você apertou o botão: {contador}")
    label.pack(pady=5)


botao = tk.Button(root, text='Aperte o botão', command=criar_label)
botao.pack(pady=20)

root.mainloop()
