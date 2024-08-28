# Clientes
from cliIUDS import Clientes
from db import db
from tkinter import *


class Clientes:
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

        self.lblendereco = Label(self.wdgt2, text="Endereço:", font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)
        self.txtendereco = Entry(self.wdgt2)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)

        self.lbltelefone = Label(self.wdgt3, text="Telefone:", font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)
        self.txttelefone = Entry(self.wdgt3)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label(self.wdgt4, text="E-mail:", font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)
        self.txtemail = Entry(self.wdgt4)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.bntInsert = Button(self.wdgt5, text="Inserir", font=self.fonte, width=15,
                                command=self.inserirCli)
        self.bntInsert.pack(side=LEFT)
        self.bntInsert = Button(self.wdgt5, text="Alterar", font=self.fonte, width=15,
                                command=self.alterarCli)
        self.bntInsert.pack(side=LEFT)
        self.bntInsert = Button(self.wdgt5, text="Excluir", font=self.fonte, width=15,
                                command=self.excluirCli)
        self.bntInsert.pack(side=LEFT)

        self.lblmsg = Label(self.wdgt6, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirCli(self):
        clie = Clientes()

        clie.cliente = self.txtnome.get()
        clie.endereco = self.txtendereco.get()
        clie.telefone = self.txttelefone.get()
        clie.email = self.txtemail.get()

        self.lblmsg["text"] = clie.insertCli()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

    def alterarCli(self):
        clie = Clientes()

        clie.idcliente = self.txtidcliente.get()
        clie.cliente = self.txtnome.get()
        clie.endereco = self.txtendereco.get()
        clie.telefone = self.txttelefone.get()
        clie.email = self.txtemail.get()

        self.lblmsg["text"] = clie.updateCli()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

    def buscarCli(self):
        clie = Clientes()

        idcliente = self.txtidcliente.get()

        self.lblmsg["text"] = clie.selectCli(idcliente)
        self.txtidcliente.delete(0, END)
        self.txtidcliente.insert(INSERT, clie.idcliente)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, clie.cliente)
        self.txtendereco.delete(0, END)
        self.txtendereco.insert(INSERT, clie.endereco)
        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT, clie.telefone)
        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, clie.email)

    def excluirCli(self):
        clie = Clientes()

        clie.idcliente = self.txtidcliente.get()

        self.lblmsg["text"] = clie.deleteCli()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)

def fetch_data():
    # Conectando ao banco de dados
    banco = db()
    c = banco.cnxao.cursor()

    # Executando uma consulta SQL para pegar todos os dados da tabela
    c.execute("SELECT * FROM tbl_cidades")
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
menubar.add_cascade(label='Arquivo', menu=interface)

# root.state("zoomed")
# interface.add_command(label='Cidade', command=Applica)
interface.add_separator()
# interface.add_command(label='Clientes', command=Quit)

# Configurando a Treeview
columns = ("ID", "Cidade", "Estado")  # Definindo as colunas
treeview = ttk.Treeview(root, columns=columns, show='headings')
for col in columns:
    treeview.heading(col, text=col)

treeview.pack(fill=tk.BOTH, expand=True)

# Pegando os dados do banco e populando a Treeview
data = fetch_data()
populate_treeview(treeview, data)

Clientes(root)
root.mainloop()