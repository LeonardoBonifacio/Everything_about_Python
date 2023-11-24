'''
Considere um programa que apresentou um erro no teste de peso de determinado produto.
Basicamente foi identificado pelos analistas que o condicional responsável por validar
a passagem de determinado produto pelas vias públicas anda calculando equivocadamente
o valor atrelado ao imposto. Desta forma, você foi contradado para resolver este problema a fim de que os valores sejam corretamente calculados. Sendo assim, desenvolva um pequeno sistema que gerencie o valor do imposto sendo de 5/100 do valor da carga, onde , a cada 10 toneladas , esse valor deve mudar, aumentando 2/100. Lembre - se de desprezar veículos não transportadores de carga , bem como não considerar os transportadores que não estão carregados.

imposto = 5/100 do valor da carga
carga em toneladas
a cada 10 toneladas + 2/100 
veiculos = normais,sem carga ou com carga.
'''
from os import system
system('cls')

print('----------IMPOSTO SOBRE CARGAS----------')

tipo_veiculo = int(input('[1] - Veiculos normais\n[2] - Veiculos cargeiros mas sem carga\n[3] - Veiculos cargeiros com carga\n->  '))

if(tipo_veiculo == 1):
    print('Este tipo de veículo não recebe imposto')
elif(tipo_veiculo == 2):
    print('Veículos descarregados não são taxados.')
elif(tipo_veiculo == 3):
    print('Por estar com carga no seu veículo você será taxado')
    qtd_carga = int(input('Digite o peso em toneladas que você está transportando: '))
    if(qtd_carga < 0):
        print('Valor inválido.') 
    elif(qtd_carga < 10):
        print('Imposto sobre essa carga = 5%')
    elif(qtd_carga >= 10):
        imposto = 5/100 + (int(qtd_carga/10) * 2/100)
        print(f'O valor do imposto foi de {imposto:.2%}')

else:     
    print('Valor inválido para tipo de veículo.')