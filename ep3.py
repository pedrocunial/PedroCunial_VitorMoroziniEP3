# -*- coding: utf-8 -*-

#Pedro Cunial & Vitor Morozini - 1A

import tkinter
import datetime

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

print('Ola ', nome,  ', voce tem ', idade, 'e mede ', altura, 'm, voce eh ', sexo, 'e seu fator de atividade fisica eh ', faf)

run = True
meses = {janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro}
cont = 1
for m in meses:
    meses(m) = i
    i += 1

while run == True:
    dia = int(input('Qual o dia referente ao alimento comido?\n'))
    mes = input('Qual o mes referente ao alimento comido?\n')
    if mes in meses:
        mes = meses(mes)
    ano = int(input('Qual o ano referente ao alimento comido?\n'))
    data = datetime.date(ano,mes,dia)
    print(data)
    
    c = True
    while c == True:
        comida = str(input('Qual o alimento comido?')).upper()
        if comida not in limpa:
            print('ERRO, a comida escolhida não está na lista de possibilidades')
        else:
            cont = 0
            for i in range(len(limpa)):
                if limpa[i][1] == comida:
                    cont += 1

            if cont > 1:
                print('ERRO, o alimento foi encontrado mais de uma vez, por favor, seja mais específico')
            else:
                c = False