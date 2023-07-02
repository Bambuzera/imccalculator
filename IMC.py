###IMPORTANTO AS BIBLIOTECAS###
import requests
from tkinter import * #neste caso "*" significar pegar tudo que tem dentro da biblioteca

###FUNCAO###
def calcimc():
    altura = pegaaltura.get()
    peso = pegapeso.get()
    altura = float(altura)
    peso = float(peso)
    IMC = (peso)/((altura/100)**2)
    textoresultado1 = f"Seu IMC é : {IMC}."
    textoresultado["text"] = textoresultado1 #coloca meu texto para aparecer dentro da janela resultado (tem que ser uma variavel "textoresultado")

###CRIANDO A PRIMEIRA JANELA###
janela = Tk()
janela.geometry("400x200")

janela.title("Calculadora de IMC") #mudar o título
textoinstrucao = Label(janela, text="Informe seus dados abaixo:") #Label("em qual janela","texto a ser exibido")
textoinstrucao.grid(column=5,row=0,padx=10,pady=10)

textoaltura = Label(janela,text="Digite sua altura em cm :")
textoaltura.grid(column=4,row=5)
pegaaltura = Entry(janela,width=20)
pegaaltura.grid(column=5,row=5,padx=10,pady=10)

textopeso = Label(janela,text="Digite sua peso em Kg : ")
textopeso.grid(column=4,row=10)
pegapeso = Entry(janela,width=20)
pegapeso.grid(column=5,row=10,padx=10,pady=10)

botao1 = Button(janela, text="Calcular", command=calcimc)
botao1.grid(column=5,row=15,padx=10,pady=10)

textoresultado = Label(janela,text="")
textoresultado.grid(column=5,row=20,padx=10,pady=10)


janela.mainloop()  #deixar a janela exibida

