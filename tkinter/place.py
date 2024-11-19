import tkinter as tk

# Configuração da janela principal
janela = tk.Tk()
janela.geometry("400x400")
janela.title("Place Layout Example")

# Adicionando labels com posicionamento absoluto
label1 = tk.Label(janela, text="Label 1", bg="red", fg="white")
label1.place(x=50, y=50)

label2 = tk.Label(janela, text="Label 2", bg="green", fg="white")
label2.place(x=150, y=150)

label3 = tk.Label(janela, text="Label 3", bg="blue", fg="white")
label3.place(x=250, y=250)

# Adicionando labels com posicionamento relativo
label4 = tk.Label(janela, text="Label 4", bg="yellow", fg="black")
label4.place(relx=0.5, rely=0.1, anchor='center')

label5 = tk.Label(janela, text="Label 5", bg="purple", fg="white")
label5.place(relx=0.5, rely=0.5, anchor='center')

label6 = tk.Label(janela, text="Label 6", bg="orange", fg="black")
label6.place(relx=0.5, rely=0.9, anchor='center')

# Executar a aplicação
janela.mainloop()

