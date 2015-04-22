# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:19:52 2015

@author: vitor_000
"""

#Pedro Cunial & Vitor Morozini - 1A

import datetime
import matplotlib.pyplot as plt



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
#
#dic = {}
#dic[0] = limpa[0]
#for i in range(1,len(limpa)):
#    for j in range(len(limpa[i])):
#        if j == 1:
#            dic[limpa[i][0]] = limpa[i][j]
#        elif j > 1:
#            dic[limpa[i][0]] += limpa[i][j]
#print(dic)

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
datas = []
cals = []
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
    datas.append(data)
    if data - datas[0] >= datetime.timedelta(weeks = 1):
        print('semana')
        run = False
    
    c = True
    while c == True:
        comida = str(input('Qual o alimento comido?')).upper()
        qtd = float(input('Qual a quantidade comida do alimento?'))
        print(comida)
        for i in range(len(limpa)):
            if limpa[i][0][0] == comida:
                print('valor computado')
                print(limpa[i][0][0])
                gramas = float(limpa[i][0][1])
                alicals = float(limpa[i][0][2])
                cals.append(qtd / gramas  * alicals)
                print(cals[-1])

                c = False
            


#Quantidade recomendada de calorias

peso = int(input('Qual o seu peso, em kg?'))

dic2 = {'minimo':1 , 'baixo':2 , 'medio':3 , 'alto':4 , 'muito ativo':5}

if faf == 1:
   coef = 1.2

if faf == 2:
   coef = 1.375
   
if faf == 3:
   coef = 1.55
   
if faf == 4:
   coef = 1.725
   
if faf == 5:
   coef = 1.9

if sexo == 'm':
    TMB = 88.36 + (13.4*peso) + (4.8*altura*100) - (5.7*idade)
else:
    TMB = 447.6 + (9.2*peso) + (3.1*altura*100)-(4.3*idade)
   

reccal = TMB*coef
   
limpa2 = []

tempo = list(range(1,8))

for i in range(7):
    limpa2.append(reccal)
 
plt.plot(tempo,limpa2)
plt.axis([1,7,0,10000])
plt.ylabel('Calorias')
plt.xlabel('Dias da semana')
plt.title(r'Quantidade de calorias recomendada')
plt.show()
 