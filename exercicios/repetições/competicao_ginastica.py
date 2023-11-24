from os import system
system('cls')

while(True):
    notas_lista = []
    maior_nota = 0
    menor_nota = 10
    media = 0
    print('-=-' * 10,'NOTAS PARA COMPETAÇÃO DE GINÁSTICA','-=-' * 10)
    nome_da_gisnasta = str(input('Digite o nome da ginasta ou tecle [ENTER] para encerrar a contagem de notas: ')).strip().title()
    if(nome_da_gisnasta == ''):
        break
    for jurado in range(7):
        notas = float(input(f'Nota do {jurado + 1}° jurado: '))
        notas_lista.append(notas)
        if(notas > maior_nota):
            maior_nota = notas
        if(notas < menor_nota):
            menor_nota = notas
    pos_maior = notas_lista.index(maior_nota)
    notas_lista.pop(pos_maior)
    pos_menor = notas_lista.index(menor_nota)
    notas_lista.pop(pos_menor)
    for notas in notas_lista:
        media += notas
    media /= 5
    print(f'<<< RESULTADO FINAL >>>\nAtleta: {nome_da_gisnasta}.\nMelhor nota: {maior_nota}\nPior nota: {menor_nota}\nMédia das notas: {media:.2f}')
print('TODAS AS NOTAS FORAM DADAS\nFIM DA COMPETIÇÃO')