#gerencia.py
from elemento import Elemento

primeiro = ultimo = None

while True:
    vl = input('Pedido ou -1 para encerrar: ')
    if vl != '-1':
        novo = Elemento(vl)
        if primeiro == None:
            primeiro = novo
            ultimo = novo
        else:
            ultimo.defineProximo(novo)
            novo.defineAnterior(ultimo)
            ultimo = novo

    else: #o usuário digitou -1 lá nin riba!
        if primeiro != None:
            #impressão da lista de pedidos
            aux = primeiro
            print('Lista de pedidos (A -> Z)')
            while aux:
                print(f'{aux}', end=' <=> ')
                aux = aux.retornaProximo()
            
            print('\n')
            aux = ultimo
            print('Lista de pedidos (Z -> A)')
            while aux:
                print(f'{aux}', end='')
                aux = aux.retornaAnterior()
        break

#======================================================
#inserir um elemento no início de uma LDE

print('Inserindo o elemento 0 no início\n')
vl = '0'
novo = Elemento(vl)
novo.defineProximo(primeiro)
primeiro.defineAnterior(novo)
primeiro = novo

aux = primeiro
while aux:
    print(f'{aux}', end=' <=> ')
    aux = aux.retornaProximo()
     

print('\nINSERINDO NO MEIO======================\n')

us = input('Digite a referência: ')
aux = primeiro
while aux:                                   #aux  novo proxAux
    if aux.valor == us: #encontrou o valor ant aux prox
        novo = Elemento('50')
        novo.defineAnterior(aux)
        novo.defineProximo(aux.retornaProximo())
        aux.retornaProximo().defineAnterior(novo)
        aux.defineProximo(novo)
        print('Valor alterado com sucesso!')
        aux = aux.retornaProximo()
    else:
        aux = aux.retornaProximo()

aux = primeiro
while aux:
    print(f'{aux}', end=' <=> ')
    aux = aux.retornaProximo()

# 10 -> 12 -> 14 -> 16 -> 18 -> 20 -> 22
#remoção dos itens de uma LDE
remove = input('\nDeseja remover: ')
if primeiro.valor == remove: #Removendo do início
    primeiro = primeiro.retornaProximo()
    primeiro.defineAnterior(None)
elif ultimo.valor == remove:#removendo do final
    ultimo = ultimo.retornaAnterior()
    ultimo.defineProximo(None)
else:
    print('\n\n\n\n')
    aux = primeiro.retornaProximo()
    encontrou = False
    while aux != ultimo:
        if aux.valor == remove: #consegue encontrar ant aux prox

            aux.retornaAnterior().defineProximo(aux.retornaProximo())
            aux.retornaProximo().defineAnterior(aux.retornaAnterior())
            aux.defineProximo(None)
            aux.defineAnterior(None)
            
            encontrou = True
            aux = aux.retornaProximo()
        else:
            aux = aux.retornaProximo()
    
    if encontrou == False:
        print('Elemento não encontrado')
    
        

print(f'Primeiro: {primeiro.valor}')
print(f'Segundo: {primeiro.retornaProximo().valor}')
aux = primeiro
while aux:
    print(f'{aux}', end=' <=> ')
    aux = aux.retornaProximo()