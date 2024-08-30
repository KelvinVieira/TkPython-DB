from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess

# Janela principal(com menus acessando todas as outras aplicações), janela login

def abrirUser():
    subprocess.Popen(['python', 'InTkPy.py'])
    root.destroy()

def abrirCid():
    subprocess.Popen(['python', 'InTkPy2.py'])
    root.destroy()

def abrirCli():
    subprocess.Popen(['python', 'InTkPy3.py'])
    root.destroy()

root = Tk()
root.title("main")

menubar = Menu(root)

root.config(menu=menubar)
interface = Menu(menubar)
menubar.add_cascade(label='Cadastros', menu=interface)

# root.state("zoomed")
interface.add_command(label='Usuário', command=abrirUser)
interface.add_separator()
interface.add_command(label='Cidade', command=abrirCid)
interface.add_separator()
interface.add_command(label='Clientes', command=abrirCli)

root.mainloop()
