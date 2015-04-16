# -*- coding: utf-8 -*-

#Pedro Cunial & Vitor Morozini - 1A

import tkinter

limpa = []
arquivo = open("alimentos.csv", encoding="latin1", mode="r+")
leitura = arquivo.readlines()

for i in leitura:
    i = i.strip()
    limpa.append(i)

for i in range(1,len(limpa)):
    limpa[i] = limpa[i].split(',')

print(limpa)
print(tkinter.__file__)
nome = str(input('Qual o seu nome?\n'))
idade = int(input('Quantos anos voce tem?\n'))
altura = str(input('Qual sua altura em metros?\n'))
altura = altura.replace(',','.')
altura = float(altura)
sexo = str(input('Qual o seu sexo (m/f)?\n')).lower()
faf = str(input('Qual o seu fator de atividade fisica (minimo,baixo,medio,alto,muito ativo)?\n')).lower()
adam = tkinter.messagebox.askquestion('ADAM','IS ADAM AN ASSHOLE?')

print('Ola ', nome,  ', voce tem ', idade, 'e mede ', altura, 'm, voce eh ', sexo, 'e seu fator de atividade fisica eh ', faf)



#for i in range(len(limpa)):