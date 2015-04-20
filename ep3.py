# -*- coding: utf-8 -*-

#Pedro Cunial & Vitor Morozini - 1A

import datetime
import tkinter.simpledialog as tk
import tkinter
root = tkinter.Tk()
root.withdraw()


limpa = []
arquivo = open("alimentos.csv", encoding="latin1", mode="r+")
leitura = arquivo.readlines()

for i in leitura:
    i = i.strip()
    limpa.append(i)

for i in range(1,len(limpa)):
    limpa[i] = limpa[i].split(',')
    limpa[i][0] = limpa[i][0].split(';')

print(limpa)
print(limpa[2][0][0])

#ENCONTREI O ERRO, ISSO NÃO É UMA MATRIZ COM VÁRIOS VALORES E SIM UMA MATRIZ COM UM VALOR SEPARANDO COM ';'

#ARRUMEI O PROBLEMA

dic = {}
dic[0] = limpa[0]
for i in range(1,len(limpa)):
    for j in range(len(limpa[i])):
        if j == 1:
            dic[limpa[i][0]] = limpa[i][j]
        elif j > 1:
            dic[limpa[i][0]] += limpa[i][j]
print(dic)

nome = str(input('Qual o seu nome?\n'))
idade = int(input('Quantos anos voce tem?\n'))
altura = str(input('Qual sua altura em metros?\n'))
altura = altura.replace(',','.')
altura = float(altura)
sexo = str(input('Qual o seu sexo (m/f)?\n')).lower()
faf = str(input('Qual o seu fator de atividade fisica (minimo,baixo,medio,alto,muito ativo)?\n')).lower()

print('Ola ', nome,  ', voce tem ', idade, 'e mede ', altura, 'm, voce eh ', sexo, 'e seu fator de atividade fisica eh ', faf)

run = True
meses = {'janeiro':1, 'fevereiro':2, 'marco':3, 'abril':4, 'maio':5, 'junho':6, 'julho':7, 'agosto':8, 'setembro':9, 'outubro':10, 'novembro':11, 'dezembro':12}

while run == True:
    dia = int(input('Qual o dia referente ao alimento comido?\n'))
    mes = input('Qual o mes referente ao alimento comido?\n')
    
    if mes in meses:
        mes = int(meses[mes])
    else:
        mes = int(mes)

    ano = int(input('Qual o ano referente ao alimento comido?\n'))

    data = datetime.date(ano,mes,dia)
    print(data)
    
    
    c = True
    while c == True:
        comida = str(input('Qual o alimento comido?')).upper()
        print(comida)
        cont = 0
        for i in range(len(limpa)):
            if limpa[i][0][0] == comida:
                print('valor computado')
                cont += 1
                print(limpa[i][0][0])
        if cont == 1:
            print('Encontrado')
            c = False
        elif cont > 1:
            print('ERRO, a comida aparece ', limpa.count(comida) ,'vezes na lista, seja mais especifico')
        else:
            print('Valor não presente na lista')
            print(cont)
