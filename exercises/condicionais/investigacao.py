'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?" "Esteve no local do crime?" "Mora perto da vítima?" "Devia para a vítima?" "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''
from os import system
system('cls')

print('-=--=-TO LHE INVESTITGANDO VIU -=--=-')

telefonou = str(input('Você telefonou para a vítima? [S] ou [N]\n>>> ')).strip().upper()
respondeu_sim = 0
if(telefonou == 'S'):
    respondeu_sim += 1
esteve_local = str(input('Esteve no local do crime? [S] ou [N]\n>>> ')).strip().upper()
if(esteve_local == 'S'):
    respondeu_sim += 1
mora_perto = str(input('Mora perto da vítima? [S] ou [N]\n>>> ')).strip().upper()
if(mora_perto == 'S'):
    respondeu_sim += 1
devia_para_vitima = str(input('Você devia para a vítima? [S] ou [N]\n>>> ')).strip().upper()
if(devia_para_vitima == 'S'):
    respondeu_sim += 1
trabalhou_com_a_vitima = str(input('Você já trabalhou com a vítima? [S] ou [N]\n>>> ')).strip().upper()
if(trabalhou_com_a_vitima == 'S'):
    respondeu_sim += 1

if(respondeu_sim == 2):
    classificacao = 'SUSPEITO VOCÊ EIN'
elif(respondeu_sim > 2 and respondeu_sim < 5):
    classificacao = 'TU FOI CÚMPLICE DESSA PORRA NÉ'
elif(respondeu_sim == 5):
    classificacao = 'TU QUE MATOU A VÍTIMA NÉ VEI'
else:
    classificacao = 'TU É INOCENTE MENOR'
print(f'Respondeu SIM a {respondeu_sim} perguntas , {classificacao}')
