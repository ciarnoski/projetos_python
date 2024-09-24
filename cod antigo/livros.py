livros = [{'titulo': 'cem anos de solidao', 'autor': 'gabriel garia marquez', 'ano de lancamento': '1982', 'favorito': '0'},
    {'titulo': 'harry potter 3', 'autor': 'jk rowling', 'ano de lancamento': '1999', 'favorito': '0'},
    {'titulo': 'primeira guerra mundial: a guerra que acabaria com todas', 'autor': 'blanc claudio', 'ano de lancamento': '2020', 'favorito': '0'}
    {'titulo': 'primeira guerra mundial: a guerra que acabaria com todas', 'autor': 'blanc claudio', 'ano de lancamento': '2020', 'favorito': '0'}]
    

for livro in livros:
    if livro['titulo'] == 'harry potter 3':
        livro['favorito'] = '1'
        print(f"Titulo: {livro['titulo']}, Autor: {livro['autor']}, Ano de lançamento: {livro['ano de lancamento']}, Favorito: {livro['favorito']}")