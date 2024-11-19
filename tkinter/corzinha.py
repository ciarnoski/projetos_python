

import random
import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("600x600")
janela.title("Canvas Example")

# Criação do canvas
canvas = tk.Canvas(janela, width=600, height=600, bg="green")
canvas.pack()

def mudar_cor(event):
    cores = ["red", "blue", "magenta", "green"]
    indice = random.randrange(0,4,1)
    canvas.config(bg=cores[indice])

janela.bind('<Return>',mudar_cor)
# olho esquerdo
canvas.create_rectangle(150, 50, 250, 150, fill="black", outline="black")

# olho direito
canvas.create_rectangle(350, 50, 450, 150, fill="black", outline="black")

#nariz
canvas.create_rectangle(250, 150, 350, 300, fill="black", outline="black")



#boca, canto esquerdo
canvas.create_rectangle(200, 200, 250, 350, fill="black", outline="black")


#boca, canto esquerdo
canvas.create_rectangle(350, 200, 400, 350, fill="black", outline="black")

janela.mainloop()


