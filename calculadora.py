#importando o tkinter
from tkinter import *
from tkinter import ttk

#cores

cor1 = "#0b0c0c" #preta
cor2 = "#ffffff" #branca
cor3 = "#38576b" #azul
cor4 = "#ECEFF1" #cinza
cor5 = "#FFAB40" #Orange/laranja


janela = Tk()
janela.title("Calculadora")
janela.geometry("235x310")
janela.config(bg=cor1)

#interface tela
frame_tela = Frame(janela, width=235, height=50, bg=cor3)
frame_tela.grid(row= 0, column=0)

#corpo
frame_corpo = Frame(janela, width=235, height=268)
frame_corpo.grid(row=1,  column=0)




#Criando Label
#Criando funçao e logica da calculadora

todos_valores = ""
valor_text = StringVar()

app_label = Label(frame_tela, textvariable=valor_text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)







def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
   
    

    #passando valor para a tela
    valor_text.set(todos_valores)

#Funcão para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_text.set(str(resultado))

#Limpando a tela
def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_text.set("")


# botoes

b_1 = Button(frame_corpo, command= limpar_tela ,text="C", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda: entrar_valores('%') ,text="%", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_corpo, command=lambda: entrar_valores('/') ,text="/", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_3.place(x=177, y=0)
numero_7 = Button(frame_corpo, command=lambda: entrar_valores('7') ,text="7", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_7.place(x=0, y=52)
numero_8 = Button(frame_corpo, command=lambda: entrar_valores('8') ,text="8", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_8.place(x=59, y=52)
numero_9 = Button(frame_corpo, command=lambda: entrar_valores('9') ,text="9", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_9.place(x=118, y=52)
b_4 = Button(frame_corpo, command=lambda: entrar_valores('*') ,text="*", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_4.place(x=177, y=52)
numero_4 = Button(frame_corpo, command=lambda: entrar_valores('4') ,text="4", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_4.place(x=0, y=104)
numero_5 = Button(frame_corpo, command=lambda: entrar_valores('5') ,text="5", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_5.place(x=59, y=104)
numero_6 = Button(frame_corpo, command=lambda: entrar_valores('6') ,text="6", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_6.place(x=118, y=104)
b_5 = Button(frame_corpo, command=lambda: entrar_valores('-') ,text="-", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_5.place(x=177, y=104)
numero_1 = Button(frame_corpo,command=lambda: entrar_valores('1') , text="1", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_1.place(x=0, y=156)
numero_2 = Button(frame_corpo, command=lambda: entrar_valores('2') ,text="2", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_2.place(x=59, y=156)
numero_3 = Button(frame_corpo, command=lambda: entrar_valores('3') ,text="3", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
numero_3.place(x=118, y=156)
b_6 = Button(frame_corpo, command=lambda: entrar_valores('+') ,text="+", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_6.place(x=177, y=156)
b_7 = Button(frame_corpo, command=lambda: entrar_valores('0') ,text="0", width=11, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=208)
b_8 = Button(frame_corpo, command=lambda: entrar_valores('.') ,text=".", width=5, height=2, bg=cor4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=118, y=208)
b_9 = Button(frame_corpo, command=calcular, text="=", width=5, height=2, bg=cor5, fg=cor2,font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE )
b_9.place(x=178, y=208)



janela.mainloop()