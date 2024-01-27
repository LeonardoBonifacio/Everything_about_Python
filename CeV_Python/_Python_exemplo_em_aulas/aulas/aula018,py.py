from os import system
system('cls')

def mensagem(texto):
    print('-' * 50)
    print(f'{texto:^50}')
    print('-' * 50)
    for c in range(3):
        print()


lista_texto = ['Aprenda python', 'Por que é ', 'Bem legal']

for item in lista_texto:
    mensagem(item)

mensagem('MOROU CARA?')


def soma(n1,n2):
    resultado = n1 + n2
    print(f'O resultado de {n1} + {n2} é  {resultado}')


soma(2,3)

soma(9,8)

soma(n1=10,n2=11)

soma(n1=11,n2=10)



def contador(*num):
    print(f'Recebi os valores {num} e são ao todo {len(num)} números.')

contador(1,2,3,4)
contador(8,0)
contador(1,2,3,4,5,6,7,8)
contador(1,2,3,4,5)


def dobrar(lista):
    print(f'Você me passou esta lista de números {lista}')
    for pos,num in enumerate(lista):
        lista[pos] = num * 2
    print(f'E eu a processei e dobrei cada elemento presente nela, {lista}')
    

dobrar([1,2,3,4,5,6])


def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} deu o resultado {s}')


soma(1,2,3,4,5)