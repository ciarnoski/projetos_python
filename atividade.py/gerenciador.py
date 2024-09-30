print('Gerenciador de Arquivos')
opcao = input('Criar turma [1]\nAcessar turma [2]\nExcluir turma [3]\n')

match opcao:
    case '1':
        print('Criando turma...')
        numturma = input('Digite o número da turma que você deseja criar: ')
        arquivo_txt = numturma + '.txt'
        with open (arquivo_txt , 'w') as arquivo:
            arquivo.write(f'turma{numturma} criada')
            print(f'Turma{numturma} criada')
    
    case '2':
        turma = input('Qual turma você deseja acessar? ')
        print(f'Acessando turma{turma}...')
        arquivo1_txt = turma + '.txt'
        print('O que você deseja fazer na turma? ')
        
        while True:
            opcao1 = input('Exibir turma [1]\nAdicionar aluno [2]\nEditar notas [3] ')
            match opcao1:
                case '1':
                    alunos = {}
                    print('Exibindo dados da turma...')
                    if not alunos:
                        print("Nenhum aluno cadastrado.")
                    else:
                        for nome, info in alunos.items():
                                notas = info.get('notas', [])
                                media = sum(notas) / len(notas) if notas else 0
                                print(f"Aluno: {nome}, Notas: {notas}, Média: {media:.2f}")
                    
                    
                    
                    
                    
                    with open (arquivo1_txt , 'r') as arquivo:
                        conteudo = arquivo.read()
                        print(conteudo)
                    break
                
                case '2':
                    print('Adicionando aluno...')
                    break
                
                case '3':
                    print('Editando notas')
                    break
                case x if x != 1 and 2 and 3:
                    print('inválido')
                    

                
        
    case '3':
        print('excluindo turma...')
    case x if x != 1 and 2 and 3:
        print('inválido')