import tkinter as tk

janela = tk.Tk()
janela.geometry("600x600")
janela.title("Canvas Example")

canvas = tk.Canvas(janela, width=600, height=600, bg="green")
canvas.pack()

canvas.create_rectangle(100, 100, 250, 250, fill="black", outline="black")

canvas.create_rectangle(500, 100, 350, 250, fill="black", outline="black")

canvas.create_rectangle(250, 250, 350, 500, fill="black", outline="black")

canvas.create_rectangle(175, 550, 250, 300, fill="black", outline="black")

canvas.create_rectangle(350, 550, 425, 300, fill="black", outline="black")

canvas.create_rectangle(0, 0, 20, 600, fill="black", outline="black")

canvas.create_rectangle(20, 600, 600, 580, fill="black", outline="black")

canvas.create_rectangle(600, 0, 580, 600, fill="black", outline="black")

canvas.create_rectangle(0, 00, 600, 20, fill="black", outline="black")



img = tk.PhotoImage(file="C:/Users/182400471/Documents/projetos_python/tkinter/penguin.png")
canvas.create_image(300, 500, image=img, anchor="center")




janela.mainloop()