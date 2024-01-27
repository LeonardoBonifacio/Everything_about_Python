lista_numeros = []
for cont_n in range(1,6):
    num = int(input(f'Digite um número inteiro: '))
    if (cont_n == 1 or num > lista_numeros[-1]):
        lista_numeros.append(num)
        print('Valor adicionado a última posição.')
    else:
        pos = 0 
        while (pos < len(lista_numeros)):
            if (num <= lista_numeros[pos]):
                lista_numeros.insert(pos, num)
                print(f'Valor adicionado a posição {pos}')
                break
            pos += 1
print(f'Sua lista ordenada {lista_numeros}')

