import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")


# Adicionando labels com posicionamento absoluto
label1 = tk.Label(janela,width=10, height=10, background="black")
label1.place(x=50, y=50)

label2 = tk.Label(janela,width=10, height=10, background="black")
label2.place(x=275, y=50)

label3 = tk.Label(janela,width= 40, height=5, background="black")
label3.place(x=50, y=250)

label4 = tk.Label(janela,width=5, height=5, background="white")
label4.place(x=50, y=50)

label5 = tk.Label(janela,width=5, height=5, background="white")
label5.place(x=275, y=50)

label6 = tk.Label(janela,width= 30, height=2, background="white")
label6.place(x=100, y=275)

label7 = tk.Label(janela,width= 10, height=20, background="pink")
label7.place(x=240, y=275)

label7 = tk.Label(janela,width= 1, height=1, background="cyan")
label7.place(x=340, y=300)
# Adicionando labels com posicionamento relativo
janela.mainloop()