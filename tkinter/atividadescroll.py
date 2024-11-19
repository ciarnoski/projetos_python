import tkinter as tk
from tkinter import ttk

class ScrollableFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
       
        # Cria o widget Canvas com a cor de fundo amarela
        self.canvas = tk.Canvas(self, background="grey")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        # Cria a barra de rolagem (Scrollbar)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
       
        # Configura o Canvas para funcionar com a barra de rolagem
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.bind('<Configure>', self.on_canvas_configure)
       
        # Cria um frame dentro do Canvas com a cor de fundo vermelha
        self.scrollable_frame = ttk.Frame(self.canvas, style="My.TFrame")
        self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
       
        # Cria uma janela dentro do Canvas que contém o frame
        self.canvas_window = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
       
        # Configura pesos das colunas e linhas do grid
        self.scrollable_frame.grid_columnconfigure(0, weight=1)
        self.scrollable_frame.grid_columnconfigure(1, weight=1)
        self.scrollable_frame.grid_rowconfigure(0, weight=1)

    def on_frame_configure(self, event):
        # Atualiza a região de rolagem do Canvas para abranger o frame interno
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        # Redimensiona o frame interno para corresponder à largura do Canvas
        self.canvas.itemconfig(self.canvas_window, width=event.width)


# Posiciona o botão na janela

class App(tk.Tk):
    def __init__(self):
        super().__init__()

       
        # Configura estilos personalizados
        style = ttk.Style()
        style.configure("My.TFrame", background="red")
       
        self.scrollable_frame = ScrollableFrame(self)
        self.scrollable_frame.pack(fill=tk.BOTH, expand=True)
        
        # Cria uma lista para armazenar os campos de entrada
        self.entries = []
        
        # Lista com perguntas para criar labels e campos de entrada
        questions = [
            "Qual seu nome?", "Quantos anos você tem?", "Onde você mora?",
            "Qual é a sua cor favorita?", "Você tem animais de estimação?",
            "Qual é o seu hobby favorito?", "Você gosta de ler?", "Qual é o seu filme favorito?",
            "Você prefere café ou chá?", "Qual é a sua comida favorita?",
            "Você já viajou para outro país?", "Qual é o seu esporte favorito?",
            "Você toca algum instrumento musical?", "Qual é a sua estação do ano preferida?",
            "Você gosta de cozinhar?", "Qual é o seu livro favorito?",
            "Você prefere praia ou montanha?", "Qual é a sua série de TV favorita?",
            "Você tem irmãos ou irmãs?", "Qual é o seu sonho de viagem?"
        ]

        for i, question in enumerate(questions):
            label = ttk.Label(self.scrollable_frame.scrollable_frame, relief="solid", text=question)
            label.grid(row=i, column=0, sticky="nsew")
            entry = ttk.Entry(self.scrollable_frame.scrollable_frame)
            entry.grid(row=i, column=1, sticky="nsew")
            self.entries.append(entry)  # Armazena cada campo de entrada

        # Cria e posiciona o botão que coleta e imprime as respostas
        button = tk.Button(self, text="Obtenha as respostas", command=self.print_respostas, bg="blue", fg="white", font=("Arial", 12), width=15)
        button.pack(pady=20)
       
    def print_respostas(self):
        # Coleta e imprime o valor de cada campo de entrada
        respostas = [entry.get() for entry in self.entries]
        for i, resposta in enumerate(respostas):
            print(f"Pergunta {i+1}: {resposta}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
