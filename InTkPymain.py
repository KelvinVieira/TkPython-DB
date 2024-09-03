from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import subprocess


def abrirUser():  # Método para a abertura da aplicação usuários
    subprocess.Popen(['python', 'InTkPy.py'])  # É usada o módulo subprocess, que abre, e executa o arquivo indicado
    root.destroy()  # Após abertura do outro arquivo, é destruída a janela(arquivo) atual

def abrirCid():  # Método para a abertura da aplicação cidades
    subprocess.Popen(['python', 'InTkPy2.py'])
    root.destroy()

def abrirCli():  # Método para a abertura da aplicação clientes
    subprocess.Popen(['python', 'InTkPy3.py'])
    root.destroy()

root = Tk()
root.title("main")

menubar = Menu(root)  # Criação do objeto menu pelo construtor Menu, com indicação de root em seu parâmetro

# Criação e configuração de menu
root.config(menu=menubar)  # Configurando em root, a variável menubar como um menu
interface = Menu(menubar)  # Variável interface recebe construtor Menu com todas as configurações de menubar
menubar.add_cascade(label='Cadastros', menu=interface) # Adciciona ao menu menubar um item menu com opção Cadastros

# root.state("zoomed")
interface.add_command(label='Usuário', command=abrirUser)  # É adicionado um item comando em interface, com nome, e o comando a ser executado
interface.add_separator()  # Adiciona um separador
interface.add_command(label='Cidade', command=abrirCid)
interface.add_separator()
interface.add_command(label='Clientes', command=abrirCli)

root.mainloop()
