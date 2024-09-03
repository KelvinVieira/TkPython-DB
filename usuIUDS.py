# Modelagem de usuário, onde é chamada a conexão ao banco de dados, realizada a coleta de dados, e manutenção de dados(Insert, Update, Delete, Select)
from db import db  # Importando o arquivo(módulo) de conexão(arquivo, apelido(classe))

class Usuarios(object):  # Classe principal
    def __init__(self, idusuario=0, nome="", telefone="", email="", usuario="", senha=""):  # Método principal (construtor)
        self.info = {}  # 
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha

    def insertUser(self): # Método de inserção de usuários
        banco = db()  # Criação do objeto do banco de dados
        try:  # Se não há excessões(código a ser executado é executado sem erro)
            c = banco.cnxao.cursor()  # Realizando a conexão por meio do objeto banco, seu módulo cnxao, e os atribuindo a c
            c.execute("insert into tbl_usuarios (usu_nome, usu_tele, usu_email, usu_usuario, usu_senha) values ('" + self.nome + "', '" +
            self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")  # Por meio do c, agora é feito a execução do comando passado no banco indicado
            banco.cnxao.commit()  # E é comitido qualquer ação pendente em banco.cnxao
            c.close()  # Fecha conexão
            return "Usuário cadastrado com sucesso!"  # Mensagem é retornada, para em que quaisquer uso, ter-se informação sobre o status de execução
        except:  # Se alguma excessão acontecer
            return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):  # Método de atualização de usuários
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("update tbl_usuarios set usu_nome = '" + self.nome + "', usu_tele = '" + self.telefone + "', usu_email = '" + self.email +
            "', usu_usuario = '" + self.usuario + "', usu_senha = '" + self.senha +
            "' where usu_id = " + self.idusuario + " ")
            banco.cnxao.commit()
            c.close()
            return "Usuário atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):  # Método de exclusão de usuários
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("delete from tbl_usuarios where usu_id = " + self.idusuario + " ")
            banco.cnxao.commit()
            c.close()
            return "Usuário excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idusuario):
        banco = db()
        try:
            c = banco.cnxao.cursor()
            c.execute("select * from tbl_usuarios where usu_id = " + idusuario + " ")
            for linha in c:  # Seleção acontecendo por meio de um laço, que olha em c para seus valores...
                self.idusuario = linha[0]  # ... e adiciona cada um de acordo
                self.nome = linha[1]
                self.telefone = linha[2]
                self.email = linha[3]
                self.usuario = linha[4]
                self.senha = linha[5]
            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
