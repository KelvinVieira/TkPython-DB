# Execução final da aplicação, e criação de todos os widgets para interface
from usuIUDS import Usuarios  # Importando arquivo classe de manutenção IUDS(Insert, Update, Delete, Select)
from db import db  # Importando arquivo classe de conexão ao banco de dados
from tkinter import *  # Importando classes Tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import subprocess


class Application:  # Classe principal
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")  # Configuração de uma fonte

        self.container1 = Frame(master)  # Criação de um widget...
        self.container1["pady"] = 10  # com suas configurações
        self.container1.pack()  # e finalizando com seu gerenciador de geometria, que decide sua posição em relação a um widget

        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")  # Texto em widget 1
        self.titulo["font"] = ("Calibri", "9", "bold")  # Com fonte definida
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2)  # Já em widget 2, além do texto acima, é criado e configurado um campo de inserção de dados para o usuário
        self.txtidusuario["width"] = 14
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)  # Com um botão para busca de informações de acordo com a informação provida pelo usuário
        self.btnBuscar["command"] = self.buscarUsuario  # Ao ser acionado, o botão realiza o comando, que por sua vez, é um método
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.container5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label(self.container6, text="Usuário:", font=self.fonte, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fonte
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container7, text="Senha:", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        # self.btn = tk.Button(self.container8, text='Cadastrar', command=self.abrir_nova_janela)
        # self.btn["font"] = self.fonte
        # self.btn.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Gravar", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirUsuario
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarUsuario
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirUsuario
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        # Configurando a Treeview
        columns = ("ID", "Nome", "Telefone", "E-mail", "Usuário","Senha")  # Definindo as colunas
        self.treeview = ttk.Treeview(root, columns=columns, show='headings')  # Criação e configuração da Treeview
        for col in columns:
            self.treeview.heading(col, text=col)  # Criação das colunas por meio de um laço
        self.treeview.bind("<<TreeviewSelect>>", self.buscarUsuarioTree)  # Ao selecionar algum item da Treeview, o método de busca é acionado
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Pegando os dados do banco e populando a Treeview
        data = fetch_data()  # Por meio do método fetch_data, a variável criada data recebe todos os valores buscados pelo método
        populate_treeview(self.treeview, data)  # E os atribui a outro método para a população desta Treeview

    def inserirUsuario(self):  # Método de inserção
        user = Usuarios()  # Criação de objeto user a partir do construtor de outro arquivo Usuarios

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

        messagebox.showinfo(  # Uso de messagebox como meio de comunicação ao usuário
            message=f"Valores inseridos com sucesso!", title="Inserção"
        )

    def alterarUsuario(self):  # Método de alteração
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

        messagebox.showinfo(
            message=f"Valores alterados com sucesso!", title="Alteração"
        )

    def excluirUsuario(self):  # Método de exclusão
        user = Usuarios()

        user.idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)

        messagebox.showinfo(
            message=f"Valores excluídos com sucesso.", title="Exclusão"
        )

    def buscarUsuario(self):  # Método de busca
        user = Usuarios()

        idusuario = self.txtidusuario.get()

        self.lblmsg["text"] = user.selectUser(idusuario)
        self.txtidusuario.delete(0, END)
        self.txtidusuario.insert(INSERT, user.idusuario)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)
        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)
        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)

    def buscarUsuarioTree(self, event):  # Método de busca da Treeview
        seleciona_item = self.treeview.selection()  # Obtém da Treeview o valor selecionado, e o atribui a variável criada
        if seleciona_item:  # Se selecionar item (não estiver null)
            # Obtém o item selecionado
            item = seleciona_item[0]
            values = self.treeview.item(item, 'values')
            # Preenche os campos de entrada com os dados do item selecionado
            self.txtidusuario.delete(0, END)
            self.txtidusuario.insert(INSERT, values[0])
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, values[1])
            self.txttelefone.delete(0, END)
            self.txttelefone.insert(INSERT, values[2])
            self.txtemail.delete(0, END)
            self.txtemail.insert(INSERT, values[3])
            self.txtusuario.delete(0, END)
            self.txtusuario.insert(INSERT, values[4])
            self.txtsenha.delete(0, END)
            self.txtsenha.insert(INSERT, values[5])

def abrirMain():  # Método já fora da classe principal para ações do menu
    subprocess.Popen(['python', 'InTkPymain.py'])  # Este em específico, usa módulo subprocess para abrir outro arquivo, e executá-lo
    root.destroy()  # Fechamento da janela atual

def fetch_data():  # Método de coleta de dados do banco para uso na Treeview
    # Conectando ao banco de dados
    banco = db()
    c = banco.cnxao.cursor()

    # Executando uma consulta SQL para pegar todos os dados da tabela
    c.execute("SELECT * FROM tbl_usuarios")
    rows = c.fetchall()  # Buscando todos os resultados
    c.close()

    return rows

# Função para popular a Treeview com os dados do banco
def populate_treeview(treeview, data):
    for row in data:
        treeview.insert("", "end", values=row)


# Definindo características da janela principal root
root = Tk()
root.title("Usuários")  # Título
menubar = Menu(root)  # Criação da variável responsável por receber o Menu com características root

# Criação e configuração de menu
root.config(menu=menubar)  # Configurando em root, a variável menubar como um menu
interface = Menu(menubar)  # Variável interface recebe menu com todas as configurações de menubar
menubar.add_cascade(label='Páginas', menu=interface)  # Adciciona ao menu menubar um item menu com opção Páginas

root.state("zoomed")  # root preenche a tela(tela-cheia)
interface.add_command(label='Principal', command=abrirMain)  # É adicionado um item comando em interface, com nome, e o comando a ser executado

# Iniciando aplicação
Application(root)
root.mainloop()
