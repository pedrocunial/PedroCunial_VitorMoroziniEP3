# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 18:19:52 2015

@author: vitor_000
"""

#Pedro Cunial & Vitor Morozini - 1A

import datetime
import matplotlib.pyplot	as plt



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
peso = int(input('Qual o seu peso, em kg?\n'))
sexo = str(input('Qual o seu sexo (m/f)?\n')).lower()
faf = str(input('Qual o seu fator de atividade fisica (minimo,baixo,medio,alto,muito ativo)?\n')).lower()

print('Ola ', nome,  ', voce tem ', idade, 'e mede ', altura, 'm, voce eh ', sexo, 'e seu fator de atividade fisica eh ', faf)

run = True
meses = {'janeiro':1, 'fevereiro':2, 'marco':3, 'abril':4, 'maio':5, 'junho':6, 'julho':7, 'agosto':8, 'setembro':9, 'outubro':10, 'novembro':11, 'dezembro':12}
datas = []
cals = [] * 7
prot = [] * 7
carb = [] * 7
gord = [] * 7

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
        if data not in datas:
            
            datas.append(data)
            if data - datas[0] >= datetime.timedelta(weeks = 1):
                print('semana completa, programa finalizado, beijos.')
                run = False
            
            comida = str(input('Qual o alimento comido?')).upper()
            qtd = float(input('Qual a quantidade comida?'))
            print(comida)
            cont = 0
            for i in range(len(limpa)):
                if limpa[i][0][0] == comida:
                    print('valor computado')
                    cont += 1
                    print(limpa[i][0][0])
                    gramas = float(limpa[i][0][1])
                    alicals = float(limpa[i][0][2])
                    aliprot = float(limpa[i][0][3])
                    alicarb = float(limpa[i][0][4])
                    aligord = float(limpa[i][0][5])
                    qtd = qtd / gramas
                    cals[data - datas[0]] = qtd * alicals
                    prot[data - datas[0]] = qtd * aliprot
                    carb[data - datas[0]] = qtd * alicarb
                    gord[data - datas[0]] = qtd * aligord
                    print(cals[-1], prot[-1], carb[-1], gord[-1])
                    c = False
        else:
            comida = str(input('Qual o alimento comido?')).upper()
            qtd = float(input('Qual a quantidade comida?'))
            print(comida)
            cont = 0
            for i in range(len(limpa)):
                if limpa[i][0][0] == comida:
                    print('valor computado')
                    cont += 1
                    print(limpa[i][0][0])
                    gramas = float(limpa[i][0][1])
                    alicals = float(limpa[i][0][2])
                    aliprot = float(limpa[i][0][3])
                    alicarb = float(limpa[i][0][4])
                    aligord = float(limpa[i][0][5])
                    qtd = qtd / gramas
                    for d in range(len(datas)):
                        if datas(d) == data:
                            cals[d] += qtd * alicals
                            prot[d] += qtd * aliprot
                            carb[d] += qtd * alicarb
                            gord[d] += qtd * aligord
                            print(cals[d], prot[d], carb[d], gord[d])
                            c = False
#Quantidade recomendada de calorias
if faf == 'minimo':
   coef = 1.2

if faf == 'baixo':
   coef = 1.375
   
if faf == 'medio':
   coef = 1.55
   
if faf == 'alto':
   coef = 1.725
   
if faf == 'muito ativo':
   coef = 1.9

if sexo == 'm':
    TMB = 88.36 + (13.4*peso) + (4.8*altura*100) - (5.7*idade)
else:
    TMB = 447.6 + (9.2*peso) + (3.1*altura*100)-(4.3*idade)
   

reccal = TMB*coef
  
limpa2 = []

tempo = list(range(1,8))

print(tempo)

for i in range(7):
    limpa2.append(reccal)
 
plt.plot(tempo,limpa2)
plt.ylabel('Calorias')
plt.xlabel('Dias da semana')
plt.title(r'Quantidade de calorias recomendada')
plt.show() 

#Quantidade ingerida de calorias

plt.plot(tempo,cals)
plt.ylabel('Calorias')
plt.xlabel('Dias da semana')
plt.title(r'Quantidade de calorias ingerida')
plt.show() 

#Quantidade ingerida de proteína

plt.plot(tempo,prot)
plt.ylabel('Proteína')
plt.xlabel('Dias da semana')
plt.title(r'Quantidade de proteína ingerida [g]')
plt.show()

#Quantidade ingerida de gordura

plt.plot(tempo,gord)
plt.ylabel('Gordura')
plt.xlabel('Dias da semana')
plt.title(r'Quantidade de gordura ingerida')
plt.show() 

#Quantidade ingerida de carboidrato

plt.plot(tempo,carb)
plt.ylabel('Carboidrato')
plt.xlabel('Dias da semana')
plt.title(r'Quantidade de carboidrato ingerida')
plt.show()  

#Índice de massa corporal Nick Trefethen 1,3 X peso (em quilogramas)/ altura (metros)

IMC = (1.3*peso) / altura

if IMC < 18.5:
   print('Você está abaixo do peso')
elif 24.9 <= IMC <= 18.5:
    print('Você é saudável')
elif 29.9 <= IMC <= 25.0:
    print('Você está com sobrepeso')
elif IMC > 30.0:
    print('Desculpe,você é considerado obeso')

#print(cals)
#print(gord)
#print(prot)
#print(carb)
