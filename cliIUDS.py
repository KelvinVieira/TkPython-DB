# Modelagem de cliente
from db import db


class Clientes(object):
    def __init__(self, idcli=0, nme="", ende="", cid="", tel="", eml=""):
        self.info = {}
        self.idcliente = idcli
        self.cliente = nme
        self.cidade = cid
        self.endereco = ende
        self.telefone = tel
        self.email = eml

    def insertCli(self):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute(
                "insert into tbl_clientes (cli_nome,cli_cid, cli_ende, cli_tele, cli_email) values ('" + self.cliente + "', '" +
                self.cidade + "', '" + self.endereco + "', '" + self.telefone + "', '" + self.email + "' )")
            banco.cnxao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateCli(self):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("update tbl_clientes set cli_nome = '" + self.nome + "', cli_cid = '" + self.cidade + "', cli_ende = '" + self.endereco + "', cli_tele = '" + self.telefone +
            "', cli_email = '" + self.email +
            "' where cli_id = " + self.idcliente + " ")
            banco.cnxao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteCli(self):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("delete from tbl_clientes where cli_id = " + self.idcliente + " ")
            banco.cnxao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectCli(self, idcliente):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("select * from tbl_clientes where cli_id = " + idcliente + " ")
            for linha in c:
                self.idcliente = linha[0]
                self.cliente = linha[1]
                self.cidade = linha[2]
                self.endereco = linha[3]
                self.telefone = linha[4]
                self.email = linha[5]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
