from os import system
system('cls')

def maior(n1,n2,n3):
    global lista_nums
    lista_nums = [n1,n2,n3]
    maior = max(lista_nums)
    return maior

result =  maior(int(input('1° número: ')),int(input('2° número: ')),int(input('3° número: ')))

print(f'O maior número entre {lista_nums} é {result}')