import tkinter
from tkinter import ttk
from tkinter import *
from PIL import *
from PIL import Image, ImageTk
import speedtest

# color:#9b70e2

branco = "#ffffff"
verde = "#00ff00"
vermelho = "#ff0000"
cinza = "#808080"
azul =  "#0000ff"
azul_claro = "#9b70e2"
preto = "#000000"
laranja = "#ff8000"
amarelo = "#ffff00"

janela = Tk()
janela.title = ""
janela.geometry('350x200')
janela.configure(background=branco)
janela.resizable(width=FALSE, height=FALSE)


#função para os dados da velocidade
def teste():
    speed = speedtest.Speedtest()
    download = f"{'{:.2f}'.format(speed.download()/1024/1024)}"
    upload = f"{'{:.2f}'.format(speed.upload()/1024/1024)}"
    print(f"download: {download}\nupload: {upload}")


    l_down_num['text'] = download
    l_up_num['text'] = upload
    b_testar['text']= "Teste novamente"
    b_testar['bg']= vermelho
    b_testar.place(x=135,y=90)

#=========================================

frame_logo = Frame(janela, width=350, height=60, bg=branco)
frame_logo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
frame_corpo = Frame(janela, width=350, height=140, bg=branco)
frame_corpo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


# COnfigurando frame logo

imagem = Image.open('verificador de velocidade\speed.png')
imagem = imagem.resize((50,50))
imagem = ImageTk.PhotoImage(imagem)

#Imagens de download e upload

down = Image.open('verificador de velocidade\down.png')
down = down.resize((30,30))
down = ImageTk.PhotoImage(down)

up = Image.open('verificador de velocidade\down.png')
up = up.resize((30,30))
up = up.rotate(180)
up = ImageTk.PhotoImage(up)

l_logo_imagem = Label(frame_logo, height=60, image=imagem, compound=LEFT, padx=10, anchor=NW, font=('Ivy 60 bold'), bg=branco, fg=preto)
l_logo_imagem.place(x=20,y=0)
l_logo_nome = Label(frame_logo,text="Speed test internet", padx=10, anchor=NE, font=('Ivy 20 bold'), bg=branco, fg=preto)
l_logo_nome.place(x=75,y=15)
l_logo_linha = Label(frame_logo,width=350, anchor=NW, font=('Ivy 2'), bg=azul_claro)
l_logo_linha.place(x=0,y=57)

#DOWNLOAD
l_down_num = Label(frame_corpo,text="",anchor=NW, font=('Arial 28'), bg=branco, fg=preto)
l_down_num.place(x=44,y=25)
l_down_frase = Label(frame_corpo,text="Mbps Download",anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
l_down_frase.place(x=30,y=70)
img_download = Label(frame_corpo, height=60, image=down, compound=LEFT, padx=10, anchor=NW, font=('Ivy 60 bold'), bg=branco, fg=preto)
img_download.place(x=60,y=100)

#UPLOAD
l_up_num = Label(frame_corpo,text="",anchor=NW, font=('Arial 28'), bg=branco, fg=preto)
l_up_num.place(x=244,y=25)
l_up_frase = Label(frame_corpo,text="Mbps Upload",anchor=NW, font=('Ivy 10'), bg=branco, fg=preto)
l_up_frase.place(x=240,y=70)
img_upload = Label(frame_corpo, height=60, image=up, compound=LEFT, padx=10, anchor=NW, font=('Ivy 60 bold'), bg=branco, fg=preto)
img_upload.place(x=260,y=100)

#Botao
b_testar = Button(frame_corpo,command=teste,text="iniciar teste",overrelief=RIDGE,relief=RAISED, font=('Ivy 10'), bg=azul_claro, fg=preto)
b_testar.place(x=144,y=80)

janela.mainloop()