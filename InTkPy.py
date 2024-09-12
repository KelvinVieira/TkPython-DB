from usuIUDS import Usuarios  # Execução final da aplicação, e criação de todos os widgets para interface
from db import db
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
import os

banco = db()
c = banco.cnxao.cursor()
class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()

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

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2, text="idUsuario:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)
        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 14
        self.txtidusuario["font"] = self.fonte
        self.txtidusuario.pack(side=LEFT)
        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarUsuario
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

        self.bntPDF = Button(self.container8, text="Criar PDF", font=self.fonte, width=15)
        self.bntPDF["command"] = self.cria_PDF
        self.bntPDF.pack(side=LEFT)

        self.bntPDF2 = Button(self.container8, text="Visualizar PDF", font=self.fonte, width=15)
        self.bntPDF2["command"] = self.ver_PDF
        self.bntPDF2.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        # Configurando a Treeview
        columns = ("ID", "Nome", "Telefone", "E-mail", "Usuário", "Senha")  # Definindo as colunas
        self.treeview = ttk.Treeview(root, columns=columns, show='headings')
        for col in columns:
            self.treeview.heading(col, text=col)
        self.treeview.bind("<<TreeviewSelect>>", self.buscarUsuarioTree)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Pegando os dados do banco e populando a Treeview
        data = fetch_data()
        populate_treeview(self.treeview, data)

    def inserirUsuario(self):
        user = Usuarios()

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

        messagebox.showinfo(
            message=f"Valores inseridos com sucesso!", title="Inserção"
        )

    def alterarUsuario(self):
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

    def excluirUsuario(self):
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

    def buscarUsuario(self):
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

    def buscarUsuarioTree(self, event):
        seleciona_item = self.treeview.selection()
        if seleciona_item:
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

    def cria_PDF(self):
        c.execute("SELECT * FROM tbl_usuarios")
        dados = c.fetchall()
        c.close()

        pdf_file = SimpleDocTemplate("usuarios.pdf")
        elements = []

        # Criar a tabela para o PDF
        column_headers = ['ID', 'Nome', 'Telefone', 'E-mail', 'Usuário', 'Senha']
        data = []
        for row in dados:
            data.append(row)

        data = [column_headers]
        for item in self.treeview.get_children():
            values = self.treeview.item(item, 'values')
            data.append(values)
        table_style = TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                  ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                                  ('FONTSIZE', (0, 0), (-1, -1), 10)])
        table = Table(data)
        table.setStyle(table_style)
        elements.append(table)

        # Adicionar a tabela ao documento e salvar
        pdf_file.build(elements)

        self.lblmsg["text"] = "PDF criado com sucesso."

        messagebox.showinfo(
            message=f"PDF criado com sucesso!", title="PDF"
        )

    def ver_PDF(self):
        try:
            os.startfile('usuarios.pdf')
            print("PDF aberto com sucesso!")
        except Exception as e:
            print(f"Erro ao abrir o PDF, não criado ou: {str(e)}")

def abrirMain():
    subprocess.Popen(['python', 'InTkPymain.py'])
    root.destroy()

def fetch_data():
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

root = Tk()
root.title("Usuários")
menubar = Menu(root)

root.config(menu=menubar)
interface = Menu(menubar)
menubar.add_cascade(label='Páginas', menu=interface)

root.state("zoomed")
interface.add_command(label='Principal', command=abrirMain)

# Iniciando aplicação
Application(root)
root.mainloop()
