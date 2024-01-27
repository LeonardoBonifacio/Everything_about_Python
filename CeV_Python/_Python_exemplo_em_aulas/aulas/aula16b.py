from os import system
system('cls')

num = [2, 5, 9, 1]
num[2] = 3 #Atribuições dessa maneira funcionam em listass
num.append(7) #Método que adiciona qualquer objeto ao final da lista
num.sort(reverse=True) #Método que ordena as listas seja de forma crescente ou descrente, também existe a função sorted() que funciona com qualquer iterável, diferentemente do método .sort()
num.insert(2, 2) #Adiciona qualquer objeto a lista em um índice específico
num.pop() #Remove ou último objeto da lista ou aquele que passarmos o seu índice nela
if (5 in num): #Meio de verificar se algum objeto se encontra na lista
    num.remove(5) # Método que remove a 1° ocorrência do objeto que passarmos como parãmetro
else:
    print('Não achei o número 5.')
print(num)
print(f'Esta lista tem {len(num)} elementos') #Len() para saber a qtd de objetos em uma lista

lista = [] #Posso criar uma lista vazia assim
lista = list() #E posso criar assim também


valores = []

valores.append(5)
valores.append(9)
valores.append(4)


for cont in range(1,6):
    valores.append(int(input(f'Digite o {cont}° valor: ')))#Um append dentro de uma estrutura de repetição para pegar valores para a lista lidos do usuário
for c,v in enumerate(valores):# Enumerate retorna o índice do objeto e o objeto em si que está sendo iterado
    print(f'Na posição {c} encontrei o valor: {v}...')
print('Chguei ao final da lista.')

a = [1, 2, 3, 4]
b = a # Fazendo desse jeito eu estou criando uma ligação entra a lista A e a lista B, e isso faz com que qualquer alterção feita em uma delas seja feita na outra também.
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

#SUPER OBSERVAÇÃO AO FAZER COM QUE UMA LISTA VAZIA RECEBA UMA CHEIA, COMO NO CASO ACIMA, VOCÊ ESTÁ LIGANDO ELAS ENTRE SI FAZENDO COM QUE QUALQUER ATRIBUIÇÃO OU ALTERAÇÃO FEITO EM UMA DELAS , SEJA EXECUTADA NA OUTRA TAMBÉM.
print('=' * 22)
#Para que isso não ocorra faça com que a lista vazia receba uma cópia da lista preenchida assim:

a = [1, 2, 3, 4]
b = a[:] #Fazendo desse jeito você está copiando todo os valores de uma lista preenchida para uma lista vazia , sem criar uma relação deligação entre elas.
print(f'Lista A: {a}')
print(f'Lista B: {b}')