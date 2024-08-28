from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

    # Login windown)
class login:
    def __init__(self):
        self.lgnwndw = tk.Tk()
        self.lgnwndw.title("Login")

        self.fnt = ("Verdana", "8")

        self.wdgt = Frame(self.lgnwndw)
        self.wdgt["padx"] = 20
        self.wdgt["pady"] = 5
        self.wdgt.pack()

        self.wdgt2 = Frame(self.lgnwndw)
        self.wdgt2["padx"] = 20
        self.wdgt2["pady"] = 5
        self.wdgt2.pack()

        self.wdgt3 = Frame(self.lgnwndw)
        self.wdgt3["padx"] = 20
        self.wdgt3["pady"] = 5
        self.wdgt3.pack()

        self.lblusuario = Label(self.lgnwndw, text="Usuário:", font=self.fnt, width=10)
        self.lblusuario.pack(side=LEFT)
        self.txtusuario = Entry(self.lgnwndw)
        self.txtusuario["width"] = 25
        self.txtusuario["font"] = self.fnt
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.lgnwndw, text="Senha:", font=self.fnt, width=10)
        self.lblsenha.pack(side=LEFT)
        self.txtsenha = Entry(self.lgnwndw)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fnt
        self.txtsenha.pack(side=LEFT)

        self.btn = tk.Button(self.lgnwndw, text='Login', command=self.verif)
        self.btn["font"] = self.fnt
        self.btn.pack(side=LEFT)

        self.lgnwndw.mainloop()

    def verif(self):
        usr = self.txtusuario.get()
        passwrd = self.txtsenha.get()
        # if usr and passwrd == :

        self.lgnwndw.mainloop()