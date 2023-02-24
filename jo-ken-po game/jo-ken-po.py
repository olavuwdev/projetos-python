import tkinter
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random


#Definindo cores

# color:#3a7676

branco = "#ffffff"
verde = "#00ff00"
vermelho = "#ff0000"
cinza = "#808080"
azul =  "#0000ff"
preto = "#000000"
laranja = "#ff8000"
amarelo = "#ffff00"


#Configurando a janela
janela = Tk()
janela.title("JO - KEN - PÔ")   
janela.geometry('260x280')
janela.configure(bg=cinza)


#Declarando funçôes logica/iniciar/terminar

global voce 
global computador 
global rondas 
global pontos_voce
global pontos_computador


pontos_voce = 0
pontos_computador = 0
rondas = 0

#logica

def jogar(i):
    global rondas 
    global pontos_voce
    global pontos_computador

    if rondas < 5:
        opcoes = ['Pedra', 'Tesoura', 'Papel']
        computador = random.choice(opcoes)
        voce = i
        opcao_computador['text'] = computador
        opcao_computador['fg'] = preto

        # caso for igual
        if voce == computador:
            print('Empate')
            l_linha['bg'] = cinza
            l_linha_c['bg'] = cinza
            l_linha_e['bg'] = amarelo
        elif voce == 'Tesoura' and computador == 'Papel':
            print('voce ganhou')   
            l_linha['bg'] = verde
            l_linha_c['bg'] = cinza
            l_linha_e['bg'] = cinza

            pontos_voce += 10
        elif voce == 'Tesoura' and computador == 'Pedra':
            print('computador ganhou')   
            l_linha['bg'] = cinza
            l_linha_c['bg'] = verde
            l_linha_e['bg'] = cinza
            pontos_computador += 10
        elif voce == 'Pedra' and computador == 'Tesoura':
            print('voce ganhou')   
            l_linha['bg'] = verde
            l_linha_c['bg'] = cinza
            l_linha_e['bg'] = cinza
            pontos_voce += 10
        elif voce == 'Pedra' and computador == 'Papel':
            print('computador ganhou')   
            l_linha['bg'] = cinza
            l_linha_c['bg'] = verde
            l_linha_e['bg'] = cinza
            pontos_computador += 10
        elif voce == 'Papel' and computador == 'Pedra':
            print('voce ganhou')   
            l_linha['bg'] = verde
            l_linha_c['bg'] = cinza
            l_linha_e['bg'] = cinza
            pontos_voce += 10
        elif voce == 'Papel' and computador == 'Tesoura':
            print('computador ganhou')   
            l_linha['bg'] = cinza
            l_linha_c['bg'] = verde
            l_linha_e['bg'] = cinza
            pontos_computador += 10

        #adicionando placa    
        l_ponto_v['text'] = pontos_voce
        l_ponto_c['text'] = pontos_computador  
        #atualizando rondas
        rondas += 1  
    else:
        l_ponto_v['text'] = pontos_voce
        l_ponto_c['text'] = pontos_computador 
        #chamando a função terminar jogo

        fim_do_jogo()    

#inicio do jogo

def iniciar_jogo():
    #configurando frame baixo
    global icon_1
    global icon_2
    global icon_3
    global b_icon_1
    global b_icon_2
    global b_icon_3

    b_jogar.destroy()
    

    icon_1 = Image.open('jo-ken-po game\pedra.png')
    icon_1 = icon_1.resize((50,50),Image.Resampling.LANCZOS)
    icon_1 = ImageTk.PhotoImage(icon_1)
    icon_2 = Image.open('jo-ken-po game\_tesoura.png')
    icon_2 = icon_2.resize((50,50),Image.Resampling.LANCZOS)
    icon_2 = ImageTk.PhotoImage(icon_2)
    icon_3 = Image.open('jo-ken-po game\papel.png')
    icon_3 = icon_3.resize((50,50),Image.Resampling.LANCZOS)
    icon_3 = ImageTk.PhotoImage(icon_3)


    b_icon_1 = Button(frame_baixo, command= lambda: jogar('Pedra'),overrelief="raise",width=50, image=icon_1, compound=CENTER, bg=cinza, fg=branco, font=("Ivy 10 bold"), anchor=CENTER, relief="flat")
    b_icon_1.place(x=15, y=60)

    b_icon_2 = Button(frame_baixo, command= lambda :jogar('Tesoura'),overrelief="raise",width=50, image=icon_2, compound=CENTER, bg=cinza, fg=branco, font=("Ivy 10 bold"), anchor=CENTER, relief="flat")
    b_icon_2.place(x=105, y=60)

    b_icon_3 = Button(frame_baixo, command= lambda :jogar('Papel'),overrelief="raise",width=50, image=icon_3, compound=CENTER, bg=cinza, fg=branco, font=("Ivy 10 bold"), anchor=CENTER, relief="flat")
    b_icon_3.place(x=195, y=60)


#terminar

def fim_do_jogo():
    global rondas 
    global pontos_voce
    global pontos_computador

    #reiniciando os pontos e o jogo
    pontos_computador = 0
    pontos_voce = 0 
    rondas = 0

    #apagandp botoes de opçpes
    b_icon_1.destroy()
    b_icon_2.destroy()
    b_icon_3.destroy()

    #definindo os vencendores 

    jogador_voce = int(l_ponto_v['text'])
    jogador_computador = int(l_ponto_c['text'])

    if jogador_voce > jogador_computador:
        app_vencedor = Label(frame_baixo, text="PARABENS, VOCE GANHOU", font=('Ivy 10 bold'),height=1, anchor="sw", bg=cinza, fg=verde)
        app_vencedor.place(x=25, y=60)
        print('Voce ganhou')
    elif jogador_computador == jogador_voce:
        app_vencedor = Label(frame_baixo, text="EMPATE", font=('Ivy 10 bold'),height=1, anchor="sw", bg=cinza, fg=preto)
        app_vencedor.place(x=25, y=60)
        print('Empate') 
    else:
        print("Computador ganhou")
        app_vencedor = Label(frame_baixo, text="NÃO FOI DESSA VEZ,\nAS MAQUINAS VENCERAM!", font=('Ivy 10 bold'),height=2, anchor="sw", fg=amarelo, bg=cinza)
        app_vencedor.place(x=30, y=60)  
    print('Jogo terminou')
    opcao_computador['text'] = ""
    l_linha['bg'] = amarelo
    l_linha_e['bg'] = amarelo
    l_linha_c['bg'] = amarelo
    
    #função para jogar novamente
    def jogar_dnv():
        l_ponto_v['text'] = '0'
        l_ponto_c['text'] = '0'
        app_vencedor.destroy()
        l_linha['bg'] = cinza
        l_linha_e['bg'] = cinza
        l_linha_c['bg'] = cinza
        b_jogar_dnv.destroy()
        iniciar_jogo()
    b_jogar_dnv = Button(frame_baixo, command=jogar_dnv , width=30,text="JOGAR", overrelief="ridge", bg=preto, fg=branco, font=("Ivy 10 bold"), anchor=CENTER, relief=RAISED)
    b_jogar_dnv.place(x=5, y=151)



#Configurando os frames

frame_cima = Frame(janela, width=260, height=100, bg=branco, relief='raised')
frame_cima.grid(row=0, column=0, sticky=NW)
frame_baixo = Frame(janela, width=260, height=300, bg=cinza, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NW)

l_voce = Label(frame_cima, text="Você", height=1, anchor="center", font=('Ivy 10'), bg=branco, fg=preto)
l_voce.place(x=45, y=70)

l_linha = Label(frame_cima, text="", width=1 ,height=10, anchor="center", bg=cinza)
l_linha.place(x=0, y=0)


l_ponto_v = Label(frame_cima, text="0", height=1, anchor="center", font=('Ivy 30 bold'), bg=branco, fg=preto)
l_ponto_v.place(x=50, y=20)

app_ = Label(frame_cima, text=":", height=1, anchor="center", font=('Ivy 30 bold'), bg=branco, fg=preto)
app_.place(x=125, y=20)

l_computador = Label(frame_cima, text="Computador", height=1, anchor="center", font=('Ivy 10'), bg=branco, fg=preto)
l_computador.place(x=170, y=70)

l_linha_c = Label(frame_cima, text="", width=1 ,height=10, anchor="center", bg=cinza)
l_linha_c.place(x=247, y=0)


l_ponto_c = Label(frame_cima, text="0", height=1, anchor="center", font=('Ivy 30 bold'), bg=branco, fg=preto)
l_ponto_c.place(x=190, y=20)


l_linha_e = Label(frame_cima,width=255,height=3, anchor="center", font=('Ivy 1 bold'), bg=cinza)
l_linha_e.place(x=0,y=91) 

opcao_computador = Label(frame_baixo, text="", height=1, anchor="center", font=('Ivy 10 bold '), bg=cinza, fg=preto)
opcao_computador.place(x=190, y=5)

 
b_jogar = Button(frame_baixo, command=iniciar_jogo, width=30,text="JOGAR", overrelief="ridge", bg=preto, fg=branco, font=("Ivy 10 bold"), anchor=CENTER, relief=RAISED)
b_jogar.place(x=5, y=151)

estilo = ttk.Style(janela)
estilo.theme_use('clam')

janela.mainloop()