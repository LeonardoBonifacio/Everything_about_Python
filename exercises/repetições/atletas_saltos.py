from os import system
system('cls')
print('-=-' * 10,'COMPETIÇÃO DE SALTO EM DISTÂNCIA','-=-' * 10)

while(True):
    saltos_lista = []
    maior_salto = 0
    menor_salto = 10
    media_saltos = 0
    nome_atleta = str(input('Digite o nome do atleta ou tecle [ENTER] para encerrar o programa: ')).strip().title()
    if(nome_atleta == ''):
        break
    for salto in range(1,6):
        distancias = float(input(f'Informe a distância alcançada com o {salto}° salto: '))
        saltos_lista.append(distancias)
        if(distancias < menor_salto):
            menor_salto = distancias
        if(distancias > maior_salto):
            maior_salto = distancias
    print(f'Atleta: {nome_atleta}.')
    print(f'Primeiro salto: {saltos_lista[0]}m')
    print(f'Segundo salto: {saltos_lista[1]}m')
    print(f'Terceiro salto: {saltos_lista[2]}m')
    print(f'Quarto salto: {saltos_lista[3]}m')
    print(f'Quinto salto: {saltos_lista[4]}m')
    print(f'Melhor salto: {maior_salto}m')
    print(f'Pior salto: {menor_salto}m')
    pos_maior = saltos_lista.index(maior_salto)
    saltos_lista.pop(pos_maior)
    pos_menor = saltos_lista.index(menor_salto)
    saltos_lista.pop(pos_menor)
    for item in saltos_lista:
        media_saltos += item
    media_saltos /= 3
    print(f'Média do saltos: {media_saltos:.2f}m')
    print(f'<<<Resultado final>>>\n{nome_atleta}: {media_saltos:.2f}m')
    input('[ENTER] - Para continuar')
    system('cls')
print('TODOS OS SALTOS FORAM DADOS\nPROGRAMA FINALIZADO COM SUCESSO')