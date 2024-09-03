import sqlite3  # Importa biblioteca sqlite3

class db:  # Classe de conexão ao banco de dados
    def __init__(self):  # Metodo principal da classe
        self.cnxao = sqlite3.connect("tkBanco.db")  # Criação de objeto variável, que recebe o construtor sqlite3, com seu método connect, e informa a este com o parâmetro do banco de dados desejado
        self.createTable()  # Execução de métodos
        self.createTableCid()
        self.createTableCli()

    def createTable(self):  # Método de criação da tabela usuários
        c = self.cnxao.cursor()  # Executa a conexão ao banco por meio da variável cnxao(que tem todos os dados do banco a ser conectado), o módulo cursor, e a atribuição a c
        c.execute("""create table if not exists tbl_usuarios (
        usu_id integer primary key autoincrement,
        usu_nome text,
        usu_tele text,
        usu_email text,
        usu_usuario text,
        usu_senha text)""")  # Com c, é feito a execução do código sql

        self.cnxao.commit()  # E com commit, é garantido a execução de algo que esteja pendente

        c.close()  # Fecha conexão

    def createTableCid(self):  # Método de criação da tabela cidades
        c = self.cnxao.cursor()
        c.execute("""create table if not exists tbl_cidades (
        cid_id integer primary key autoincrement,
        cid_nome text,
        cid_esta text)""")

        self.cnxao.commit()

        c.close()

    def createTableCli(self):  # Método de criação da tabela clientes
        c = self.cnxao.cursor()
        c.execute("""create table if not exists tbl_clientes (
        cli_id integer primary key autoincrement,
        cli_nome text,
        cli_cid text,
        cli_ende text,
        cli_tele text,
        cli_email text)""")

        self.cnxao.commit()

        c.close()
