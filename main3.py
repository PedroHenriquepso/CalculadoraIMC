from tkinter import *
from tkinter import ttk
import tkinter as tk

#-----------cores------------

co0 ='#ffffff' #white
co1 ='#444466' #bluish-gray
co2 ='#4065a1' #blue
co3 ='#000000' #black
co4 ='#FFA500' #orange


def on_entry_click(event, entry, default_text):
    if entry.get() == default_text:
        entry.delete(0, tk.END)  # Remove o texto de exemplo
        entry.config(fg='black')  # Altera a cor do texto para preto

def on_focus_out(event, entry, default_text):
    if entry.get() == '':
        entry.insert(0, default_text)
        entry.config(fg='#888888')  # Altera a cor do texto para cinza mais claro

def criar_entry_com_texto_exemplo(frame, default_text, proximo_widget):
    entry = tk.Entry(frame, fg='#888888')  # Define a cor do texto para cinza mais claro
    entry.insert(0, default_text)
    entry.bind("<FocusIn>", lambda event: on_entry_click(event, entry, default_text))
    entry.bind("<FocusOut>", lambda event: on_focus_out(event, entry, default_text))
    return entry

janela = tk.Tk()
janela.title('PedroDev')
janela.geometry('300x350')
janela.configure(bg='white')

#----------dividindo a JANELA em duas partes--------

frame_cima = tk.Frame(janela, width=300, height=50, bg='#ffffff', pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=tk.NSEW)

frame_baixo = tk.Frame(janela, width=300, height=300, bg='#ffffff', pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=tk.NSEW)

#----------configurando FRAME CIMA--------

app_nome = tk.Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('ivy 16 bold'), bg='#ffffff', fg='#000000')
app_nome.place(x=0, y=0)

app_linha = tk.Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('ivy 1'), bg='#000000', fg='#000000')
app_linha.place(x=0, y=35)

#----------Calcular peso ideal--------
    
def calcular_peso_ideal(altura):
   peso_ideal = 25 * altura**2 #formula para calcular o peso ideal
   return peso_ideal

#---------------Funçao Calcular--------------
def calcular(event=None):


    peso = float(e_peso.get())
    altura = float(e_altura.get())

    imc = peso / altura**2

    resultado = imc

    if resultado < 18.5:
       l_resultado_text['text'] = "Seu IMC é: Abaixo do peso"

    elif resultado >= 18.5 and resultado < 24.9:
       l_resultado_text['text'] = "Seu IMC é: Normal"

    elif resultado >= 24.9 and resultado < 30:
       l_resultado_text['text'] = "Seu IMC é: Sobrepeso"

    else:
       l_resultado_text['text'] = "Seu IMC é: Obesidade"


    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

#----------Calcula peso ideal e exibe--------

    peso_ideal = calcular_peso_ideal(altura)
    l_peso_ideal['text'] = "Seu peso ideal é: {:.{}f} kg".format(peso_ideal, 2)

    #----------configurando FRAME BAIXO--------

l_peso = tk.Label(frame_baixo, text='INSIRA SEU PESO:', height=1, padx=0, relief='flat', anchor='center', font=('ivy 10 bold'), bg='#ffffff', fg='#000000')
l_peso.grid(row=0, column=0, sticky=tk.NSEW, pady=10, padx=3)
e_peso = tk.Entry(frame_baixo, fg='#888888')
e_peso.insert(0, 'Ex. 60')
e_peso.grid(row=0, column=1, sticky=tk.NSEW, pady=10, padx=3)
e_peso.bind("<FocusIn>", lambda event: on_entry_click(event, e_peso, 'Ex. 60'))
e_peso.bind("<FocusOut>", lambda event: on_focus_out(event, e_peso, 'Ex. 60'))
e_peso.bind("<Return>", lambda event: e_altura.focus_set())

l_altura = tk.Label(frame_baixo, text='INSIRA SUA ALTURA:', height=1, padx=0, relief='flat', anchor='center', font=('ivy 10 bold'), bg='#ffffff', fg='#000000')
l_altura.grid(row=1, column=0, sticky=tk.NSEW, pady=10, padx=3)
e_altura = tk.Entry(frame_baixo, fg='#888888')
e_altura.insert(0, 'Ex. 1.65')
e_altura.grid(row=1, column=1, sticky=tk.NSEW, pady=10, padx=3)
e_altura.bind("<FocusIn>", lambda event: on_entry_click(event, e_altura, 'Ex. 1.65'))
e_altura.bind("<FocusOut>", lambda event: on_focus_out(event, e_altura, 'Ex. 1.65'))
e_altura.bind("<Return>", calcular)


l_resultado = Label(frame_baixo, text='------',width=4, height=1, padx=5,pady=12, relief='flat', anchor='center', font=('ivy 24 bold'), bg=co0, fg=co3)
l_resultado.place(x=200, y=10)

b_calcular_Button = Button(frame_baixo,command=calcular, text='Calcular',width=35, height=1, relief='raised', anchor='center', font=('ivy 10 bold'), bg=co2, fg=co3)
b_calcular_Button.grid(row=2, column=0, sticky=NSEW, pady=10,padx=5, columnspan=20)

l_resultado_text = Label(frame_baixo, text='',width=35, height=1, padx=0,pady=5, relief='flat', anchor='w', font=('ivy 10 bold'), bg=co0, fg=co3)
l_resultado_text.grid(row=3, column=0, sticky=NSEW, pady=5,padx=5, columnspan=20)

#----------janela de exibir peso ideal--------
l_peso_ideal = Label(frame_baixo, text='', width=35, height=1, padx=0, pady=5, relief='flat', anchor='w', font=('ivy 10 bold'), bg=co0, fg=co3)
l_peso_ideal.grid(row=4, column=0, sticky=NSEW, pady=5, padx=5, columnspan=20)

janela.mainloop()
