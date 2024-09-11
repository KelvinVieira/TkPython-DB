# Modelagem de cidade
from db import db

class Cidades(object):
    def __init__(self, idcid=0, cdd="", etdo=""):
        self.info = {}
        self.idcidade = idcid
        self.cidade = cdd
        self.estado = etdo

    def insertCid(self):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("insert into tbl_cidades (cid_nome, cid_esta) values ('" + self.cidade + "', '" + self.estado + "' )")
            banco.cnxao.commit()
            c.close()
            return "Usuário cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def updateCid(self):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("update tbl_cidades set cid_nome = '" + self.cidade + "', cid_esta = '" + self.estado +
            "' where cid_id = " + self.idcidade + " ")
            banco.cnxao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteCid(self):
        banco = db()
        c = banco.cnxao.cursor()
        c.execute("SELECT cl.cli_cid, ci.cid_nome FROM tbl_clientes cl INNER JOIN tbl_cidades ci ON cl.cli_cid = ci.cid_nome WHERE cl.cli_cid = " + self.cidade + " ")
        # SELECT us.usu_cid, ci.cid_nome FROM tbl_usuario us INNER JOIN tbl_cidade ci ON us.usu_cid = ci.cid_nome WHERE us.usu_cid = 'Jataí'
        r = c.fetchall()
        if r:
            return "Componente cidade já é utilizado por outra tabela. Não é possível fazer exclusão!"
        else:
            try:
                c.execute("delete from tbl_cidades where cid_id = " + self.idcidade + " ")
                banco.cnxao.commit()
                c.close()
                return "Valores excluídos com sucesso!"
            except:
                return "Ocorreu um erro na exclusão do usuário"

    def selectCid(self, idcidade):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("select * from tbl_cidades where cid_id = " + idcidade + " ")
            for linha in c:
                self.idcidade = linha[0]
                self.nome = linha[1]
                self.estado = linha[2]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
