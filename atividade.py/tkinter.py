import os
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext

class GerenciadorTurmas:
    def __init__(self, master):
        self.master = master
        self.master.title("Gerenciador de Turmas")

        self.alunos = {}

        # Criação dos botões
        tk.Button(master, text='Criar Turma', command=self.criar_turma).pack(pady=10)
        tk.Button(master, text='Acessar Turma', command=self.acessar_turma).pack(pady=10)
        tk.Button(master, text='Excluir Turma', command=self.excluir_turma).pack(pady=10)
        
        self.text_area = scrolledtext.ScrolledText(master, width=50, height=15)
        self.text_area.pack(pady=10)

    def criar_turma(self):
        numturma = simpledialog.askstring("Criar Turma", "Digite o número da turma que você deseja criar:")
        if numturma:
            arquivo_txt = f"{numturma}.txt"
            if os.path.exists(arquivo_txt):
                messagebox.showwarning("Erro", "Turma já existe.")
            else:
                with open(arquivo_txt, 'w') as arquivo:
                    messagebox.showinfo("Sucesso", f'Turma {numturma} criada.')

    def acessar_turma(self):
        turma = simpledialog.askstring("Acessar Turma", "Qual turma você deseja acessar?")
        if turma:
            arquivo_txt = f"{turma}.txt"
            if not os.path.exists(arquivo_txt):
                messagebox.showwarning("Erro", "Turma não existe.")
                return
            
            while True:
                opcao1 = simpledialog.askstring("Opções", "O que você deseja fazer na turma?\n1. Exibir turma\n2. Adicionar aluno\n3. Editar notas\n4. Sair")
                
                if opcao1 == '1':
                    self.exibir_turma(arquivo_txt)
                elif opcao1 == '2':
                    self.adicionar_aluno(arquivo_txt)
                elif opcao1 == '3':
                    self.editar_notas(arquivo_txt)
                elif opcao1 == '4':
                    break
                else:
                    messagebox.showwarning("Erro", "Opção inválida.")
    
    def exibir_turma(self, arquivo_txt):
        self.text_area.delete(1.0, tk.END)  # Limpa a área de texto
        with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            self.text_area.insert(tk.END, conteudo)

    def adicionar_aluno(self, arquivo_txt):
        nome_aluno = simpledialog.askstring("Adicionar Aluno", "Digite o nome do aluno:")
        notas_str = simpledialog.askstring("Adicionar Notas", "Digite as notas separadas por espaço (ex: 8.0 7.5 9.0):")
        if nome_aluno and notas_str:
            try:
                notas = list(map(float, notas_str.split()))
                media = sum(notas) / len(notas)
                with open(arquivo_txt, 'a', encoding='utf-8') as arquivo:
                    arquivo.write(f"\nAluno: {nome_aluno}, Notas: {notas}, Média: {media:.2f}\n")
                messagebox.showinfo("Sucesso", f"Aluno {nome_aluno} adicionado.")
            except ValueError:
                messagebox.showwarning("Erro", "Por favor, insira notas válidas.")

    def editar_notas(self, arquivo_txt):
        aluno_para_editar = simpledialog.askstring("Editar Notas", "Digite o nome do aluno que você deseja editar as notas:")
        if aluno_para_editar:
            with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
                conteudo = arquivo.readlines()

            alunos = {}
            for linha in conteudo:
                if "Aluno:" in linha:
                    partes = linha.split(',')
                    nome_aluno = partes[0].split(': ')[1]
                    notas_str = partes[1].split(': ')[1].strip().strip('[]')
                    notas = list(map(float, notas_str.split()))
                    media = sum(notas) / len(notas) if notas else 0
                    alunos[nome_aluno] = {'notas': notas, 'média': media}

            if aluno_para_editar in alunos:
                novas_notas_str = simpledialog.askstring("Novas Notas", "Digite as novas notas separadas por espaço:")
                if novas_notas_str:
                    try:
                        novas_notas = list(map(float, novas_notas_str.split()))
                        media_nova = sum(novas_notas) / len(novas_notas) if novas_notas else 0
                        
                        alunos[aluno_para_editar]['notas'] = novas_notas
                        alunos[aluno_para_editar]['média'] = media_nova
                        
                        with open(arquivo_txt, 'w', encoding='utf-8') as arquivo:
                            for aluno, dados in alunos.items():
                                arquivo.write(f"Aluno: {aluno}, Notas: {dados['notas']}, Média: {dados['média']:.2f}\n")
                        
                        messagebox.showinfo("Sucesso", f"As notas do aluno {aluno_para_editar} foram atualizadas.")
                    except ValueError:
                        messagebox.showwarning("Erro", "Por favor, insira notas válidas.")
            else:
                messagebox.showwarning("Erro", "Aluno não encontrado.")

    def excluir_turma(self):
        turma = simpledialog.askstring("Excluir Turma", "Qual turma você deseja excluir?")
        if turma:
            arquivo_txt = f"{turma}.txt"
            if os.path.exists(arquivo_txt):
                os.remove(arquivo_txt)
                messagebox.showinfo("Sucesso", f'Turma {turma} excluída.')
            else:
                messagebox.showwarning("Erro", "Turma não existe.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GerenciadorTurmas(root)
    root.mainloop()
