from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk, Image
import string
import random

# cores ---------------------------------------------
cor0 = "#444466" # Preta
cor1 = "#feffff" # Branca
cor2 = "#f05a43" # Vermelha

janela = Tk()
janela.title(' ')
janela.geometry('295x350')
janela.configure(bg=cor1)

estilo = ttk.Style(janela)
estilo.theme_use('clam')


# Dividindo a janela em dois frames ---------------------------------------------------- 
frame_cima = Frame(janela, width=295, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

# Trabalhando no frame de cima --------------------------------------------------------
img = Image.open('senha.png')
img = img.resize((20,20), Image.LANCZOS)
img = ImageTk.PhotoImage(img)

app_logo = Label(frame_cima, image=img, height=60, compound=LEFT, padx=10, relief='flat', anchor='nw', bg=cor1)
app_logo.place(x=2, y=0)

app_nome = Label(frame_cima, text= 'GERADOR DE SENHAS', width=20, height=1, padx=0, relief='flat', anchor='nw', bg=cor1, fg=cor0, font=('Ivy 16 bold'))
app_nome.place(x=25, y=2)

app_linha = Label(frame_cima, text= '', width=295, height=1, padx=0, relief='flat', anchor='nw', bg=cor2, fg=cor0, font=('Ivy 1'))
app_linha.place(x=0,y=35)

# Fução gerar senha -------------------------------------------------------------------------
def criar_senha():
    alfabeto_maior = string.ascii_uppercase
    alfabeto_menor = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    global combinar
    # condição maiúscula
    if estado_1.get() == alfabeto_maior:
        combinar = alfabeto_maior
    else:
      pass
    # condição minúscula
    if estado_2.get() == alfabeto_menor:
        combinar = combinar + alfabeto_menor
    else:
      pass
    # condição números
    if estado_3.get() == numeros:
        combinar = combinar + numeros
    else:
      pass
    # condição simbolos
    if estado_4.get() == simbolos:
        combinar = combinar + simbolos
    else:
      pass

    comprimento = int(spin.get())
    senha = ''.join(random.sample(combinar, comprimento))
    app_senha['text'] = senha

    def copiar_senha():
      info = senha
      frame_baixo.clipboard_clear()
      frame_baixo.clipboard_append(info)

      messagebox.showinfo('Senha copiada', 'A senha foi copiada para a área de transferência')
      
    botao_copiar_senha = Button(frame_baixo,command=copiar_senha, text= 'Copiar', width=7, height=2, relief='raised', overrelief='solid' ,anchor='center', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
    botao_copiar_senha.grid(row=0, column=1, sticky=NW, padx=5, pady=5, columnspan=1) 





# Trabalhando no frame de baixo--------------------------------------------------------
app_senha = Label(frame_baixo, text= '- - -', width=20, height=2, padx=0, relief='solid', anchor='center', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_senha.grid(row=0, column=0, sticky=NSEW, columnspan=1, padx=3, pady=10)

app_info = Label(frame_baixo, text= 'Número total de caracteres na senha', height=1, padx=0, relief='flat', anchor='nw', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_info.grid(row=1, column=0, sticky=NSEW, columnspan=2, padx=5, pady=1)

var= IntVar()
var.set(0)
spin = Spinbox(frame_baixo, from_=0, to=20, width=5, textvariable=var)
spin.grid(row=2, column=0, sticky=NW, columnspan=2, padx=5, pady=8)


alfabeto_maior = string.ascii_uppercase
alfabeto_menor = string.ascii_lowercase
numeros = string.digits
simbolos = string.punctuation

frame_caracteres = Frame(frame_baixo, width=295, height=210, bg=cor1, pady=0, padx=0, relief='flat')
frame_caracteres.grid(row=3, column=0, sticky=NSEW, columnspan=3)

#-----------------------letras maiuscúlas--------------------------------------------	
estado_1 = StringVar()
estado_1.set(False)
check_1 = Checkbutton(frame_caracteres, width=1, var=estado_1, onvalue=alfabeto_maior, offvalue='off',relief='flat', bg=cor1)
check_1.grid(row=0, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text= 'ABC Letras maiúsculas', height=1, padx=0, relief='flat', anchor='nw', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_info.grid(row=0, column=1, sticky=NW, padx=2, pady=5)

#-----------------------letras minuscúlas--------------------------------------------	
estado_2 = StringVar()
estado_2.set(False)
check_2 = Checkbutton(frame_caracteres, width=1, var=estado_2, onvalue=alfabeto_menor, offvalue='off',relief='flat', bg=cor1)
check_2.grid(row=1, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text= 'abc Letras minuscúlas', height=1, padx=0, relief='flat', anchor='nw', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_info.grid(row=1, column=1, sticky=NW, padx=2, pady=5)

#-----------------------Números--------------------------------------------	
estado_3 = StringVar()
estado_3.set(False)
check_3 = Checkbutton(frame_caracteres, width=1, var=estado_3, onvalue=numeros, offvalue='off',relief='flat', bg=cor1)
check_3.grid(row=3, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text= '123 Números', height=1, padx=0, relief='flat', anchor='nw', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_info.grid(row=3, column=1, sticky=NW, padx=2, pady=5)

#-----------------------Símbolos--------------------------------------------	
estado_4 = StringVar()
estado_4.set(False)
check_4 = Checkbutton(frame_caracteres, width=1, var=estado_4, onvalue=simbolos, offvalue='off',relief='flat', bg=cor1)
check_4.grid(row=4, column=0, sticky=NW, padx=2, pady=5)
app_info = Label(frame_caracteres, text= '!@# Símbolos', height=1, padx=0, relief='flat', anchor='nw', bg=cor1, fg=cor0, font=('Ivy 10 bold'))
app_info.grid(row=4, column=1, sticky=NW, padx=2, pady=5)

#-----------------------Botao--------------------------------------------
botao_gerar_senha = Button(frame_caracteres, command=criar_senha ,text= 'GERAR SENHA', width=28, height=1, relief='flat', overrelief='solid' ,anchor='center', bg=cor2, fg=cor1, font=('Ivy 10 bold'))
botao_gerar_senha.grid(row=5, column=0, sticky=NSEW, padx=5, pady=20, columnspan=5)



  

janela.mainloop()

