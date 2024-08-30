import sqlite3

class db:  # Classe de conexão ao banco de dados
    def __init__(self):
        self.cnxao = sqlite3.connect("tkBanco.db")
        self.createTable()
        self.createTableCid()
        self.createTableCli()

    def createTable(self):  # + Cliente, cidade
        c = self.cnxao.cursor()
        c.execute("""create table if not exists tbl_usuarios (
        usu_id integer primary key autoincrement,
        usu_nome text,
        usu_tele text,
        usu_email text,
        usu_usuario text,
        usu_senha text)""")

        self.cnxao.commit()

        c.close()

    def createTableCid(self):  # + Cliente, cidade
        c = self.cnxao.cursor()
        c.execute("""create table if not exists tbl_cidades (
        cid_id integer primary key autoincrement,
        cid_nome text,
        cid_esta text)""")

        self.cnxao.commit()

        c.close()

    def createTableCli(self):  # + Cliente, cidade
        c = self.cnxao.cursor()
        c.execute("""create table if not exists tbl_clientes (
        cli_id integer primary key autoincrement,
        cli_nome text,
        cli_ende text,
        cli_tele text,
        cli_email text)""")

        self.cnxao.commit()

        c.close()
