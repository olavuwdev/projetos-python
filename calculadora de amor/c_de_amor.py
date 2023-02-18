#Calculadora de amor

#importando biblioteca

from tkinter import *
from tkinter import Tk, ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter
import random

#Definindo cores

preto = "#000000"
azul = "#000fe6"
amarelo = "#a6e600"
branco = '#feffff'
cinza = "#bdc7bc"
co5 = '#e06636'
co7 = '#3fbfb9' #verde
vermelho = '#ff0000'
rosa = "#f03e3e"


#Criando Janela
janela = Tk()
janela.title("")
janela.geometry("410x400")
janela.configure(background=branco)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use('clam')


#frames

frame_cima = Frame(janela, width=418, height=200, bg=branco)
frame_cima.grid(row=0, column=0)

frame_meio = Frame(janela, width=418, height=200, bg=branco, relief='solid')
frame_meio.grid(row=1, column=0)

#---------- logo -------------


# Funçao calcular

def calcular_amor():
    #pegando nomes
     
    nome1 = e_seu_nome.get()
    nome2 = e_parceiro_nome.get()

    if nome1 == "" and nome2 == "":
        tkinter.messagebox.showinfo(title="Atenção", message="Preencha os campos: Seu nome e Nome da parceiro(a).",)

    #Valores contera digitos entre 0-9
    else:
        st = "0123456789"

        #resultado sera em dois digitos

        digitos = 2

        #variavel que contem o resultado

        resultado = "".join(random.sample(st, digitos))
        
        l_resulado['text'] = "Porcentagem de amor entre"
        l_resulado_1['text'] = nome1 +" & " +nome2
        l_resulado_2['text'] = resultado + "%"
  


app = Label(frame_cima, text="Calculadora do Amor", width=400, padx=5, anchor=NW, font=('Fixedsys 20'), bg=cinza, fg=branco)
app.place(x=0, y =0)

#Adicianando Imagem

#Funçao para escolher opções

def escolher():
    #variaveis globais
    global app_img, app_img_love

    escolhar_1 = selecionado_1.get()
    escolhar_2 = selecionado_2.get()

    if escolhar_1 == 'Homem' and escolhar_2 == 'Mulher':
        imagem = "calculadora de amor/casal2.png"
        imagem_2 = "calculadora de amor/heart2.png"
    elif escolhar_1 == 'Homem' and escolhar_2 == 'Homem':
        imagem = "calculadora de amor/casal1.png"
        imagem_2 = "calculadora de amor/heart-lbgt.png"
    elif escolhar_1 == 'Mulher' and escolhar_2 == 'Mulher':
        imagem = "calculadora de amor/casal3.png"
        imagem_2 = "calculadora de amor/heart-lbgt.png"
    elif escolhar_1 == 'Mulher' and escolhar_2 == 'Homem':
        imagem = "calculadora de amor/casal2.png"
        imagem_2 = "calculadora de amor/heart2.png"
    else:
        print("Selecione os generos")
        return    

    #abrindo imagem casal
    app_img = Image.open(imagem)
    app_img = app_img.resize((140,140))
    app_img =ImageTk.PhotoImage(app_img)
    app_logo['image'] = app_img
    #abrindo imagem botao
    app_img_love = Image.open(imagem_2)
    app_img_love = app_img_love.resize((30,30))
    app_img_love =ImageTk.PhotoImage(app_img_love)
    botao_calcular['image'] = app_img_love


app_img = Image.open('calculadora de amor\heart.png')
app_img = app_img.resize((140,140))
app_img =ImageTk.PhotoImage(app_img)

app_logo = Label(frame_cima,image=app_img, width=400,compound=LEFT, padx=5, anchor=NW, bg=branco)
app_logo.place(x=10, y =50)


#Resultados --------------

l_resulado = Label(frame_cima, text="", width=35, padx=10, anchor=NW, font=('verdana 10'), bg=branco, fg=preto)
l_resulado.place(x=170, y =70)

l_resulado_1 = Label(frame_cima, text="", width=17, padx=10, anchor=CENTER, font=('verdana 13 bold'), bg=branco, fg=vermelho)
l_resulado_1.place(x=170, y =100)

l_resulado_2 = Label(frame_cima, text="%", width=5, padx=10, anchor=CENTER, font=('verdana 25 bold'), bg=branco, fg=preto)
l_resulado_2.place(x=210, y =140)

#frame meio ---------------------

l_nome = Label(frame_meio, text="Seu nome", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
l_nome.place(x=6, y =15)

e_seu_nome = Entry(frame_meio, width=15, font=('Ivy 14'), justify='center', relief='solid')
e_seu_nome.place(x=10,y=40)

selecionado_1 = StringVar()

rad_1 = Radiobutton(frame_meio, command= escolher,text='Homem', bg=branco, font=('Ivy 10'), value="Homem", variable=selecionado_1).place(x=10, y=80)
rad_2 = Radiobutton(frame_meio, command= escolher, text='Mulher', bg=branco, font=('Ivy 10'), value="Mulher", variable=selecionado_1).place(x=10, y=105)

l_linha = Label(frame_meio, width=1, height=10, anchor=NW, font=('verdana 1 bold'), bg=preto, fg=preto)
l_linha.place(x=190, y =40)
l_linha = Label(frame_meio, width=1, height=10, anchor=NW, font=('verdana 1 bold'), bg=vermelho, fg=preto)
l_linha.place(x=200, y =40)

l_nome = Label(frame_meio, text="Nome da Parceiro(a)", anchor=NW, font=('Ivy 10 bold'), bg=branco, fg=preto)
l_nome.place(x=217, y =15)

e_parceiro_nome = Entry(frame_meio, width=15, font=('Ivy 14'), justify='center', relief='solid')
e_parceiro_nome.place(x=220,y=40)

selecionado_2 = StringVar()

rad_3 = Radiobutton(frame_meio,  command= escolher,text='Homem', bg=branco, font=('Ivy 10'), value="Homem", variable=selecionado_2).place(x=220, y=80)
rad_4 = Radiobutton(frame_meio, command= escolher, text='Mulher', bg=branco, font=('Ivy 10'), value="Mulher", variable=selecionado_2).place(x=220, y=105)

# Botao Calcular ------------------

app_img_love = Image.open('calculadora de amor\heart2.png')
app_img_love = app_img_love.resize((30,30))
app_img_love =ImageTk.PhotoImage(app_img_love)

botao_calcular = Button(frame_meio, command=calcular_amor,image = app_img_love,text="Calcular amor".upper(), width=200, compound=LEFT, anchor=CENTER, font=('Ivy 10 bold'), bg=rosa, fg=preto)
botao_calcular.place(x=110, y =140)




janela.mainloop()