import tkinter as tk

root = tk.Tk()

# Cria um frame para conter os widgets
frame = tk.Frame(root, width=300, height=200)
frame.pack_propagate(False)  # Impede que o frame redimensione para caber os widgets
frame.pack()

# Cria um label e usa anchor para posicioná-lo
label = tk.Label(frame, text="Olá, Tkinter!", bg="lightblue")
label.pack(anchor="nw",expand=True)  # Âncora no canto superior esquerdo (noroeste)

root.mainloop()