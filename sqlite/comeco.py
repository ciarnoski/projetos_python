import sqlite3

conn =""
def connect_data_base():#caminho do banco
    db_name='exemplo.db'
    global conn
    conn = sqlite3.connect(db_name)#comando que conecta e cria o banco
    create_table()

def create_table_produtos():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY,
            nome_produto TEXT NOT NULL,
            codbarras INTEGER
        )
    ''')

def create_table():
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            idade INTEGER
        )
    ''')
    conn.commit()

def inserir_usuario(nome, idade):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO usuarios (nome, idade)
        VALUES (?, ?)
    ''', (nome, idade))
    conn.commit()

def selecionar_usuarios():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM usuarios')
    return cursor.fetchall()

def list_all_tables():
    cursor = conn.cursor()
    # Listar todas as tabelas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabelas = cursor.fetchall()
    for tabela in tabelas:
        print(tabela[0])
    conn.commit()

def fechar_conexao():
    conn.close()

connect_data_base()
create_table()
create_table_produtos()
inserir_usuario("abacate",35)
print(selecionar_usuarios())
list_all_tables()
fechar_conexao()

