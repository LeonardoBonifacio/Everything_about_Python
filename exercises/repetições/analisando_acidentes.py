from os import system
system('cls')
media_veiculos = qtd_cidades_menos_2000_veiculos = media_acidentes_cidades_menos_2000 = 0
for cidades in range(1,6):
    print('-=-' * 6,'COLETANDO INFORMAÇÕES SOBRE ACIDENTES DE TRÂNSITOS', '-=-' * 6)
    print('-=-' * 7,cidades,'° cidade','-=-' * 7)
    codigo_cidade = str(input('Digite o CEP da sua cidade no formato [xxxxx-xxx]: ')).strip()
    numero_veiculos_passeio = int(input('Digite o número de veículos de passeio que essa cidade possuia em 1999: '))
    qtd_aci_tran_viti = int(input('Digite o número de acidentes de trânsito com vítmas que essa cidade teve em 1999: '))
    if(cidades == 1):
        maior_indice = qtd_aci_tran_viti
        menor_indice = qtd_aci_tran_viti
        cep_maior_indice = codigo_cidade
        cep_menor_indice = codigo_cidade
    if(qtd_aci_tran_viti > maior_indice):
        maior_indice = qtd_aci_tran_viti
        cep_maior_indice = codigo_cidade
    if(qtd_aci_tran_viti < menor_indice):
        menor_indice = qtd_aci_tran_viti
        cep_menor_indice = codigo_cidade
    if(numero_veiculos_passeio < 2000):
        qtd_cidades_menos_2000_veiculos += 1
        media_acidentes_cidades_menos_2000 += qtd_aci_tran_viti
    media_veiculos += numero_veiculos_passeio
    system('cls')
media_veiculos /= 5
media_acidentes_cidades_menos_2000 /= qtd_cidades_menos_2000_veiculos
print('-=-' * 10,'RELATÓRIO','-=-' * 10)
print(f'Em 1999 o maior de indíce de acidentes foi da cidade  com cep {cep_maior_indice} com {maior_indice} acidentes\nEnquanto o menor índice de acidentes foi da cidade com cep {cep_menor_indice} com {menor_indice} acidentes.')
print(f'A média de veículos que essas cinco cidades possuem juntas é de {media_veiculos:.2f}')
print(f'A média de acidentes nas cidades que possuiam menos de 2000 veiculos é de {media_acidentes_cidades_menos_2000:.2f}')