# -*- coding: utf-8 -*-

#Pedro Cunial & Vitor Morozini - 1A

import tkinter

limpa = []
arquivo = open("alimentos.csv", "r+")
leitura = arquivo.readlines()
#print(leitura)

for i in leitura:
    #i =i.replace("\n","")
    i = i.strip()
    limpa.append(i)
#print(limpa)

for i in range(1,len(limpa)):
    limpa[i] = limpa[i].split(',')

print(limpa)
print(tkinter.__file__)
nome = str(input('Qual o seu nome?\n'))
idade = int(input('Quantos anos você tem?\n'))
altura = str(input('Qual sua altura em metros?\n'))
altura = altura.replace(',','.')
altura = float(altura)
sexo = str(input('Qual o seu sexo (m/f)?\n')).lower()
faf = str(input('Qual o seu fator de atividade física (minimo,baixo,médio,alto,muito ativo)?\n')).lower()

print(nome)



#for i in range(len(limpa)):