from os import system
system('cls')
'''
#Interactive help 
help(print)

#Mostra o doc interno de qualquer comando
#Que é quase igual ao help

print(print.__doc__)

#Criar Docstrings

def contador(i,f,p):
    """
    -> Faz um contagem e mostra na tela
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return : sem retorno
    Função criada por Leonardo Bonifácio da rua da casa dele
    """
    c = i
    while(c <= f):
        print(f'{c}', end=' ')
        c += 1
    print('FIM!')

contador(2,10,2)

help(contador)


#Parâmetro opcionais

def somar(a = 0, b = 0, c = 0):
    """
    -> Faz a soma de trÊs valores e mostra o resultado na tela.
    :param a: o primeiro valor, por padrão é 0
    :param b: o segundo valor, por padrão é 0
    :param c: o terceiro valor, por padrão é 0
    :return : sem retorno
    Função criada por Leonardo Bonifácio
    """
    s = a + b + c
    if(s != 0):
        print(f'A Soma vale {s}')
    else:
        print(f'Nenhum valor foi passado logo a soma vale 0.')

somar(3,2,4)
somar(8,4)
somar(b=4,c=2)
somar()
  


#Escopo de variáveis

def teste1():
    x = 8
    print(f'Na função teste, x vale {x}')
    print(f'Na função teste, n vale {n}')

#Programa principal
n = 2
teste1()
print(f'No programa principal, n vale {n}')
print(f'No programa principal, x vale {x}')
'''
'''
def teste2(b):
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

#Programa principal

a = 5
teste2(a)
print(f'A fora vale {a}')'''

'''def funcao():
    n = 3
    print(f'N dentro da função vale {n}')

n = 1
funcao()
print(f'N no programa principal vale {n}')'''
'''
def teste3(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste3(a)
print(f'A fora vale {a}')
'''

'''#Retornando valores para usá-los de forma mais prática 

def somar(a = 0,b = 0, c= 0):
    s = a + b + c
    return s

r1 = somar(1, 2, 3)
r2 = somar(1,7)
r3 = somar(4)
print(f'Meus cáclculos deram {r1}, {r2} e {r3}')'''

#prática da aula
'''
def fatorial(num = 1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f

numero = int(input('Digite um número para saber o fatorial - > '))


print(f'O fatorial de {numero} é {fatorial(numero)}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()

print(f'Os outros resultados foram {f1}, {f2} e {f3}')'''


def par_ou_par(n = 0):
    if(n == 0):
        return 'Zero não é nem par e nem impar'
    elif(n % 2 == 0):
        return True
    else:
        return False

num = int(input('Digite um número: '))

if(par_ou_par(num) == True):
    print('É par')
elif(par_ou_par(num) == False):
    print('É impar')
else:
    print(par_ou_par(num))