#login
from tkinter import *
from tkinter import messagebox
import subprocess
from db import db

class login:
    def __init__(self, master):
        self.fnt = ("Verdana", "8")

        self.wdgt = Frame(master)
        self.wdgt["padx"] = 20
        self.wdgt["pady"] = 5
        self.wdgt.pack()

        self.wdgt2 = Frame(master)
        self.wdgt2["padx"] = 20
        self.wdgt2["pady"] = 5
        self.wdgt2.pack()

        self.wdgt3 = Frame(master)
        self.wdgt3["padx"] = 20
        self.wdgt3["pady"] = 5
        self.wdgt3.pack()

        self.lblusuario = Label(self.wdgt, text="Usuário:", font=self.fnt, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.wdgt)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fnt
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.wdgt2, text="Senha:", font=self.fnt, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.wdgt2)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fnt
        self.txtsenha.pack(side=LEFT)

        self.btn = Button(self.wdgt3, text='Login', command=self.verif)
        self.btn["font"] = self.fnt
        self.btn.pack(side=LEFT)

    def verif(self):
        banco = db()
        c = banco.cnxao.cursor()

        usr = self.txtusuario.get()
        passwrd = self.txtsenha.get()
        c.execute('SELECT usu_usuario, usu_senha FROM tbl_usuarios WHERE usu_usuario=? AND usu_senha=?', (usr, passwrd))
        resultado = c.fetchone()

        if resultado:
            messagebox.showinfo('Sucesso', 'Login realizado com sucesso!')
            # Aqui você pode adicionar a lógica para abrir uma nova janela ou realizar outras ações
            self.txtusuario.delete(0, END)
            self.txtsenha.delete(0, END)

            self.opnMain()
            root.destroy()

        else:
            messagebox.showerror('Erro', 'Usuário ou senha inválidos! Tente novamente.')

    def opnMain(self):
        subprocess.Popen(['python', 'InTkPymain.py'])


root = Tk()
root.title("Login")
login(root)
root.mainloop()
