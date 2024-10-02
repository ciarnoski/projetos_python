import os
alunos = {}
print('Gerenciador de Arquivos')

opcao = input('Criar turma [1]\nAcessar turma [2]\nExcluir turma [3]\n')

match opcao:
    case '1':
        print('Criando turma...')
        numturma = input('Digite o número da turma que você deseja criar: ')
        arquivo_txt = numturma + '.txt'
        with open (arquivo_txt , 'w') as arquivo:
            print(f'Turma {numturma} criada')
        
    case '2':
        turma = input('Qual turma você deseja acessar? ')
        print(f'Acessando turma{turma}...')
        arquivo1_txt = turma + '.txt'
        print('O que você deseja fazer na turma? ')
        
        while True:
            opcao1 = input('Exibir turma [1]\nAdicionar aluno [2]\nEditar notas [3]\nSair [4] ')
            match opcao1:
                case '1':
                    alunos = {}
                    print('Exibindo dados da turma...')
                    with open (arquivo1_txt , 'r', encoding='utf-8') as arquivo:
                        conteudo = arquivo.read()
                        print(conteudo)
                    
                
                case '2':
                    print("Adicionando aluno...")
                    nome_aluno = input("Digite o nome do aluno:\n")
                    notas = input("Digite as notas separadas por espaço (ex: 8.0 7.5 9.0):\n").split()
                    notas = [float(nota) for nota in notas]
                    media = sum(notas) / len(notas)
                    alunos[nome_aluno] = {'notas': notas, 'média': media}

                    with open(arquivo1_txt, 'a', encoding='utf-8') as arquivo:
                        arquivo.write(f"\nAluno: {nome_aluno}, Notas: {notas}, Média: {media:.2f}\n")
                    
                case '3':
            
                    print('Editando notas')
                    
                    with open(arquivo1_txt, 'r', encoding='utf-8') as arquivo:
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

                    
                    aluno_para_editar = input("Digite o nome do aluno que você deseja editar as notas:\n")
                    
                    if aluno_para_editar in alunos:
                        novas_notas = input("Digite as novas notas separadas por espaço (ex: 8.0 7.5 9.0):\n").split()
                        novas_notas = [float(nota) for nota in novas_notas]
                        media_nova = sum(novas_notas) / len(novas_notas) if novas_notas else 0
                        
                        
                        alunos[aluno_para_editar]['notas'] = novas_notas
                        alunos[aluno_para_editar]['média'] = media_nova
                        
                        
                        with open(arquivo1_txt, 'w', encoding='utf-8') as arquivo:
                            for aluno, dados in alunos.items():
                                arquivo.write(f"Aluno: {aluno}, Notas: {dados['notas']}, Média: {dados['média']:.2f}\n")
                        
                        print(f"As notas do aluno {aluno_para_editar} foram atualizadas.")
                    else:
                        print("Aluno não encontrado.")
                
                                    
                case '4':
                    print('Saindo...')
                    break
                
                
                
                case x if x != 1 and 2 and 3:
                    print('inválido')
                    
    case '3':
        
        turma = input('Qual turma você deseja excluir? ')
        print('Excluindo turma...')
        arquivo = turma + '.txt'
        os.remove(arquivo)
        print(f'Turma {turma} excluída')
    
    case x if x != 1 and 2 and 3:
        print('inválido')