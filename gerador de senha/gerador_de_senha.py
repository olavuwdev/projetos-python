from tkinter import *
import tkinter
import random
from tkinter import ttk
import pyperclip as pc
from tkinter import messagebox

janela = Tk()
janela.geometry("300x410")

cores = "color : #ffffff"
#cores 
cinza = "#008080"
vermelho = "#ff0000"
branco = "#ffffff"

#Funçao para copiar o texto
def copiar():
    copia = senhacod['text']
    pc.copy(copia)
    tkinter.messagebox.showinfo(message=" Senha copiada para area de transferencia")

#Funçao para a gerar senha segura.
def gerar_senha():
    texto = entre.get()
    lowc = texto.lower()
    upperc = texto.upper()
    number = '1234567890'
    caracters = '*&$#@!*()+{^`'
    size = 12

    key = lowc + upperc + number + caracters

    password = "".join(random.sample(key, size))  
    senhacod['text'] = password

    print(password)
    boton_copiar = Button(framecima,command=copiar,text="COPIAR", width=5, height=1,overrelief= 'ridge', justify=CENTER )
    boton_copiar.place(x=230, y=195)

framecima = Frame(janela,width=300, height=410, bg=cinza)
framecima.grid(row=0, column=0)

texto1 = Label(framecima, text="Gerador de senhas seguras",width=30, anchor=CENTER, padx=10, font=('verdana 11 bold'),justify=CENTER, bg=branco)
texto1.place(x=0, y=10)

texto2 = Label(framecima, text="Informe uma palavra \n para sem embaralhada na senha",width=30, height=2,anchor=SW, font=('verdana 9'),justify=CENTER, bg=cinza)
texto2.place(x=50, y=40)
entre =Entry(framecima,justify=CENTER)
entre.place(x=100, y=80) 


botao = Button(framecima,command=gerar_senha,text="Gerar senha", width=17, height=1,overrelief= 'ridge', justify=CENTER)
botao.place(x=100, y=120)

senhacod = Label(framecima, text="", width=17,height=2)
senhacod.place(x=100, y=190)





'''a1 = "Hey, nice to see you"
pc.copy(a1)
'''

janela.mainloop()