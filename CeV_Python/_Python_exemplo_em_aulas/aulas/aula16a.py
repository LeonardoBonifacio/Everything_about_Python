from os import system
system('cls')
#TUPLAS
#lanche = 'Hambuerguer' <-- Exemplo de variavel simples
#TUPLAS SÃO IMUTÁVEIS ou seja 'tuple' object does not suport item assignment

#Comandos impossiveis em tuplas
'''lanche[1] = 'outra coisa' ou ''
lanche.pop()
lanche.remove('qualquer coisa que esteja dentro do tupla')
'''
#Tuplas podem ser atribuidas em parentese como abaixo:
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
#Como podem ser atribuidas sem parenteses tambem
#lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Fritra'
print(f'A {len(lanche)} items nessa tupla e...')#len() para saber a qtd de itens
print()
for pos,comida  in enumerate(lanche):
#A ordem das variaveis de iteração faz diferença no que elas receberão em uma iteração, por exemplo como eu coloquei a variavel pos em 1° lugar ela receberá a primeira atribuição(enumerate)  e como coloquei a variavel comida em 2° lugar ela receberá a segunda atribuição(lanche) em cada iteração.
#enumerate basicamente retorna o indice de alguma objeto da lista,tupla ou dicionário
    print(f'Eu vou comer {comida} na posição {pos}')

print()
for cont in range(0,len(lanche)):
   print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

print()

for comida in lanche:
    print(f'Eu vou comer {comida}.')
print('Comi pra caramba')

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b#concatenação de tuplas

print(c.count(4))#Contar quantos elementos tem dentro da tupla

print(c.index(2))#retorna a posição da 1° ocorrencia do elemento '2' na tupla

print(c.index(2,2))#retorna a posição da 1° ocorrência do elemento '2' na tupla apartir da 2 posição.

humano = ('Leo', 19, 'M', 70.70)#Assim como as listas , as tuplas podem armazenar ao mesmo tempo  diferentes tipos de objetos no python.

del(humano)#função del apaga da memória qualquer coisa que esteja dentro de uma variável, unico meio de modificar uma tupla é excluindo tudo que há dentro dela


nums = (4, 3, 2, 1)
print(sorted(nums))#Ordena a tupla
lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
print(sorted(lanche))#Ordena a tupla, sendo de forma alfabética ou numérica

#Estudar funçoes enumerate e zip para tuplas

vendedores = ('Leo', 'Celeste')
vendas = ('10000', '15000')

for vendedor,venda in zip(vendedores,vendas):
    print(vendedor)
    print(venda)

seasons = ('Spring', 'Summer', 'Fall', 'Winter')
print(tuple(enumerate(seasons)))
print(tuple(enumerate(seasons, start=1)))


x = [1, 2, 3]
y = [4, 5, 6]
list(zip(x, y))
print(list(zip(x,y)))
x2, y2 = zip(*zip(x, y))
print(x2,y2)

#enumerate ainda tem um parametro pra definir a partir de que número ele começa que é o start = int
#enumerate(lanche,start = 1)





























'''
As tuplas aceitam a mesma forma de fatiamento de strings como:
print(lanche[0])
print(lanche[1:])
print(lanche[::2])
print(lanche[-1])
print(lanche[::-1])
print(lanche[-1::-2])
LEMBRANDO QUE O PYTHON SEMPRE IGNORA O ULTIMO ELEMENTO EM UM FATIAMENTO DE STRINGS OU OUTROS TIPOS DE VARIAVEIS COMPOSTAS
'''
