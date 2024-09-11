# Cidade
from cidIUDS import Cidades
from db import db
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess

#Não deixar excluír cidade se estiver sendo usada em Clientes, criar impressão dos dados dos cadastros em arquívo PDF, e permitir visualizar o mesmo, em todos os cadastros
class CidadE:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.wdgt1 = Frame(master)
        self.wdgt1["pady"] = 10
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

        self.lblidcidade = Label(self.wdgt1, text="idCidade:", font=self.fonte, width=10)
        self.lblidcidade.pack(side=LEFT)
        self.txtidcidade = Entry(self.wdgt1)
        self.txtidcidade["width"] = 14
        self.txtidcidade["font"] = self.fonte
        self.txtidcidade.pack(side=LEFT)
        self.btnBuscar = Button(self.wdgt1, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarCid
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.wdgt2, text="Cidade:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)
        self.txtnome = Entry(self.wdgt2)
        self.txtnome["width"] = 26
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblest = Label(self.wdgt3, text="Estado:", font=self.fonte, width=10)
        self.lblest.pack(side=LEFT)
        self.comboest = ttk.Combobox(self.wdgt3, state="readonly",
            values=["AM", "AC", "AL", "GO", "SP", "MG"], width=27
        )
        self.comboest.pack()

        self.bntInsert = Button(self.wdgt4, text="Inserir", font=self.fonte, width=15,
                                command=self.inserirCid)
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.wdgt4, text="Alterar", font=self.fonte, width=15)
        self.bntAlterar["command"] = self.alterarCid
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.wdgt4, text="Excluir", font=self.fonte, width=15)
        self.bntExcluir["command"] = self.excluirCid
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.wdgt5, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        # Configurando a Treeview
        columns = ("ID", "Cidade", "Estado")  # Definindo as colunas
        self.treeview = ttk.Treeview(root, columns=columns, show='headings')
        for col in columns:
            self.treeview.heading(col, text=col)
        self.treeview.bind("<<TreeviewSelect>>", self.buscarCidadeTree)
        self.treeview.pack(fill=tk.BOTH, expand=True)

        # Pegando os dados do banco e populando a Treeview
        data = fetch_data()
        populate_treeview(self.treeview, data)

    def inserirCid(self):
        cids = Cidades()

        cids.cidade = self.txtnome.get()
        cids.estado = self.comboest.get()

        self.lblmsg["text"] = cids.insertCid()

        self.txtnome.delete(0, END)
        self.comboest.delete(0, END)

        messagebox.showinfo(
            message=f"Valores adicionados com sucesso!",  # {self.txtnome}
            title="Inserção"
        )

    def alterarCid(self):
        cids = Cidades()

        cids.idcidade = self.txtidcidade.get()
        cids.cidade = self.txtnome.get()
        cids.estado = self.comboest.get()

        self.lblmsg["text"] = cids.updateCid()

        self.txtidcidade.delete(0, END)
        self.txtnome.delete(0, END)
        self.comboest.delete(0, END)

        messagebox.showinfo(
            message=f"Valores alterados com sucesso!", title="Alteração"
        )

    def excluirCid(self):
        cids = Cidades()

        cids.cidade = self.txtnome.get()
        cids.idcidade = self.txtidcidade.get()

        self.lblmsg["text"] = cids.deleteCid()

        self.txtidcidade.delete(0, END)
        self.txtnome.delete(0, END)
        self.comboest.delete(0, END)

        messagebox.showinfo(
            message=f"Valores excluídos com sucesso.", title="Exclusão"
        )

    def buscarCid(self):
        cids = Cidades()

        idcidade = self.txtidcidade.get()

        self.lblmsg["text"] = cids.selectCid(idcidade)
        self.txtidcidade.delete(0, END)
        self.txtidcidade.insert(INSERT, cids.idcidade)
        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, cids.nome)
        self.comboest.insert(INSERT, cids.estado)

    def buscarCidadeTree(self, event):
        seleciona_item = self.treeview.selection()
        if seleciona_item:
            # Obtém o item selecionado
            item = seleciona_item[0]
            values = self.treeview.item(item, 'values')
            # Preenche os campos de entrada com os dados do item selecionado
            self.txtidcidade.delete(0, END)
            self.txtidcidade.insert(INSERT, values[0])
            self.txtnome.delete(0, END)
            self.txtnome.insert(INSERT, values[1])
            self.comboest.delete(0, END)
            self.comboest.insert(INSERT, values[2])

def abrirMain():
    subprocess.Popen(['python', 'InTkPymain.py'])
    root.destroy()

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
menubar.add_cascade(label='Páginas', menu=interface)

root.state("zoomed")
interface.add_command(label='Principal', command=abrirMain)


CidadE(root)
root.mainloop()
