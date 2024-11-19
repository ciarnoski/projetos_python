import tkinter as tk

# Criar a janela principal
root = tk.Tk()
root.title("Exemplo de Rolagem Horizontal")
root.geometry("400x100")
# Criar uma Scrollbar horizontal
canvas = tk.Canvas(root)
scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
scrollbar.pack(side="bottom", fill="x", expand=True)

# Criar o Canvas

canvas.pack(side="top", expand=True)



# Configurar o Canvas para usar a Scrollbar
canvas.config(xscrollcommand=scrollbar.set)

# Criar um Frame dentro do Canvas
frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Adicionar itens ao Frame
for i in range(100):
    button = tk.Button(frame, text=f"Item {i+1}")
    button.pack(side="left")

# Atualizar a largura do canvas quando o frame mudar
def update_scroll_region(event):
    canvas.config(scrollregion=canvas.bbox("all"))

frame.bind("<Configure>", update_scroll_region)

# Iniciar o loop principal
root.mainloop()