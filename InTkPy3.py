# Clientes
from cliIUDS import Clientes
from db import db
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

class Cliente:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.wdgt = Frame(master)
        self.wdgt["pady"] = 10
        self.wdgt["pady"] = 5
        self.wdgt.pack()

        self.wdgt1 = Frame(master)
        self.wdgt1["pady"] = 10
        self.wdgt1["pady"] = 5
        self.wdgt1.pack()

        self.wdgt2 = Frame(master)
        self.wdgt2["padx"] = 20
        self.wdgt2["pady"] = 5
        self.wdgt2.pack()

        self.wdgt3 = Frame(master)
        self.wdgt3["padx"] = 20
        self.wdgt3["pady"] = 5
        self.wdgt3.pack()

        self.wdgt4 = Frame(master)
        self.wdgt4["padx"] = 20
        self.wdgt4["pady"] = 5
        self.wdgt4.pack()

        self.wdgt5 = Frame(master)
        self.wdgt5["padx"] = 20
        self.wdgt5["pady"] = 5
        self.wdgt5.pack()

        self.wdgt6 = Frame(master)
        self.wdgt6["padx"] = 20
        self.wdgt6["pady"] = 5
        self.wdgt6.pack()

        self.wdgt7 = Frame(master)
        self.wdgt7["padx"] = 20
        self.wdgt7["pady"] = 5
        self.wdgt7.pack()

        self.lblidcliente = Label(self.wdgt, text="idCliente:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=LEFT)
        self.txtidcliente = Entry(self.wdgt)
        self.txtidcliente["width"] = 14
        self.txtidcliente["font"] = self.fonte
        self.txtidcliente.pack(side=LEFT)
        self.btnBuscar = Button(self.wdgt, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCli
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.wdgt1, text="Cliente:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.wdgt1)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblCidade = Label(self.wdgt2, text="Cidade:", font=self.fonte, width=10)
        self.lblCidade.pack(side=LEFT)
        self.comboCid = ttk.Combobox(self.wdgt2, state="", width=11)  # Outra criação de combobox, porém...
        self.comboCid.pack(side=LEFT)
        self.bntInsert = Button(self.wdgt2, text="Busca cidade", font=self.fonte, width=12,
                                command=self.popular_combobox)  # ... populado por um método, conectado a base de dados, mas, somente apartir da seleção deste botão
        self.bntInsert.pack(side=RIGHT)

        self.lblendereco = Label(self.wdgt3, text="Endereço:", font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)
        self.txtendereco = Entry(self.wdgt3)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)

        self.lbltelefone = Label(self.wdgt4, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.wdgt4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.wdgt5, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.wdgt5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.bntInsert = Button(self.wdgt6, text="Inserir", font=self.fonte, width=15,
                                command=self.inserirCli)
        self.bntInsert.pack(side=LEFT)
        self.bntInsert = Button(self.wdgt6, text="Alterar", font=self.fonte, width=15,
                                command=self.alterarCli)
        self.bntInsert.pack(side=LEFT)
        self.bntInsert = Button(self.wdgt6, text="Excluir", font=self.fonte, width=15,
                                command=self.excluirCli)
        self.bntInsert.pack(side=LEFT)

        self.lblmsg = Label(self.wdgt7, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        # Configurando a Treeview
        columns = ("ID", "Nome", "Endereço", "Telefone", "E-mail")  # Definindo as colunas
        self.treeview = ttk.Treeview(root, columns=columns, show='headings')
        for col in columns:
            self.treeview.heading(col, text=col)
        self.treeview.bind("<<TreeviewSelect>>", self.buscarClienteTree)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Pegando os dados do banco e populando a Treeview
        data = fetch_data()
        populate_treeview(self.treeview, data)


    def inserirCli(self):
        clie = Clientes()

        clie.cliente = self.txtnome.get()
        clie.cidade = self.comboCid.get()
        clie.endereco = self.txtendereco.get()
        clie.telefone = self.txttelefone.get()
        clie.email = self.txtemail.get()

        self.lblmsg["text"] = clie.insertCli()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.comboCid.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

        messagebox.showinfo(
            message=f"Valores inseridos com sucesso!", title="Inserção"
        )

    def alterarCli(self):
        clie = Clientes()

        clie.idcliente = self.txtidcliente.get()
        clie.cliente = self.txtnome.get()
        clie.cidade = self.comboCid.get()
        clie.endereco = self.txtendereco.get()
        clie.telefone = self.txttelefone.get()
        clie.email = self.txtemail.get()

        self.lblmsg["text"] = clie.updateCli()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.comboCid.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

        messagebox.showinfo(
            message=f"Valores alterados com sucesso!", title="Alteração"
        )

    def excluirCli(self):
        clie = Clientes()

        clie.idcliente = self.txtidcliente.get()

        self.lblmsg["text"] = clie.deleteCli()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.comboCid.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

        messagebox.showinfo(
            message=f"Valores excluídos com sucesso.", title="Exclusão"
        )

    def buscarCli(self):
        clie = Clientes()

        idcliente = self.txtidcliente.get()

        self.lblmsg["text"] = clie.selectCli(idcliente)
        self.txtidcliente.delete(0, END)
        self.txtidcliente.insert(INSERT, clie.idcliente)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, clie.cliente)
        self.comboCid.delete(0, END)
        self.comboCid.insert(INSERT, clie.cidade)
        self.txtendereco.delete(0, END)
        self.txtendereco.insert(INSERT, clie.endereco)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, clie.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, clie.email)

    def buscarClienteTree(self, event):
        seleciona_item = self.treeview.selection()
        if seleciona_item:
            # Obtém o item selecionado
            item = seleciona_item[0]
            values = self.treeview.item(item, 'values')
            # Preenche os campos de entrada com os dados do item selecionado
            self.txtidcliente.delete(0, END)
            self.txtidcliente.insert(INSERT, values[0])
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, values[1])
            self.comboCid.delete(0, END)
            self.comboCid.insert(INSERT, values[2])
            self.txtendereco.delete(0, END)
            self.txtendereco.insert(INSERT, values[3])
            self.txttelefone.delete(0, END)
            self.txttelefone.insert(INSERT, values[4])
            self.txtemail.delete(0, END)
            self.txtemail.insert(INSERT, values[5])

    def popular_combobox(self):  # Método para população da combobox...
        # Conectar ao banco de dados
        banco = db()  # ... com conexão ao banco de dados(feita a partir do arquivo classe db) permitindo a combobox ter somente valores do mesmo
        c = banco.cnxao.cursor()

        # Executar a consulta
        c.execute("SELECT cid_nome FROM tbl_cidades")
        resul = c.fetchall()

        # Popular o ComboBox
        for r in resul:
            self.comboCid.insert('end', r[0])

        c.close()

def abrirMain():
    subprocess.Popen(['python', 'InTkPymain.py'])
    root.destroy()

def fetch_data():
    # Conectando ao banco de dados
    banco = db()
    c = banco.cnxao.cursor()

    # Executando uma consulta SQL para pegar todos os dados da tabela
    c.execute("SELECT * FROM tbl_clientes")
    rows = c.fetchall()  # Buscando todos os resultados
    c.close()

    return rows

    # Função para popular a Treeview com os dados do banco
def populate_treeview(treeview, data):
    for row in data:
        treeview.insert("", "end", values=row)

root = Tk()
menubar = Menu(root)

root.config(menu=menubar)
interface = Menu(menubar)
menubar.add_cascade(label='Páginas', menu=interface)

root.state("zoomed")
interface.add_command(label='Principal', command=abrirMain)


Cliente(root)
root.mainloop()
