'''
Functions em iterables


Basicamente alguns métodos e funções que já existem no python podem rodar uma function para cada item, da mesma forma que fizemos com list comprehension

map function
basicamente o que a função map faz é aplicar uma função pra cada item do seu iterable

Estrutura
lista = list(map(função, iterable_original))

'''

'''
Exemplo: digamos que eu tenha um function que corrige um código de um produto


def padronizar_texto(texto):
    texto = texto.casefold()
    texto = texto.replace("  "," ")
    texto = texto.strip()
    return texto

produtos = [' ABC12 ', 'abc34', 'AbC37', 'beb12', ' BSA151', 'BEB23']


# fazendo com for

for i, produto in enumerate(produtos):
    produtos[i] = padronizar_texto(produto)
print(produtos)

# fazendo com a function map
produtos_padronizados = list(map(padronizar_texto, produtos)) # ele pega cada objeto dentro do iterable e passa como parametro da função automaticamente

# sempre é necessário usar o map dentro de um list() pois o map gera um objeto map que não é muito visível(a não ser pelo espaço de memória que ele está ocupando no momento)

print(produtos_padronizados)

'''

'''
sort(ou sorted) com function


produtos = ['apple tv', 'mac', 'IPhone x', 'IPhone 11', 'IPad', 'apple watch', 'mac book', 'airpods']
# o sort tem um parametro(key=) que aceita uma função a ser aplicada em cada objeto dentro da lista(que o sort esta ordenando) antes dele ordenar, mas sem alterar a lista original.
# mesmo conceito da map function que aplica uma função em cada objeto de uma lista, porém o sort tem uma sacada a mais pois ele ordena os itens depois de aplicar a função em todos eles

produtos.sort(key=str.casefold)
# pra usar um função/método específico de tipos de objeto diferentes no python sem necessariamente ter o objeto explicitamente escrito, é necessário passar a função que define o tipo desse objeto como: str,list,dict,int,float,tuple,set

print(produtos)

'''

'''
# passando segundo item de um tupla como valor a ser ordenado pelo sort


vendas_produtos = {'vinho': 100, 'cafeteira': 149, 'microondas': 300, 'iphone': 7000}

lista_vendas = list(vendas_produtos.items()) # trasnformando o dict em uma lista, pois o dicionário nao pode ser ordenado
# método items() trasnforma cada par de chave/valor de um dict em uma tupla com dois items(chave e o valor)

def pegar_segundo_item(tupla):
    return tupla[1]
lista_vendas.sort(key=pegar_segundo_item,reverse=True) # aqui por exemplo nesse sort a key para ordenar está sendo o segundo item de cada tupla em minha lista de tuplas, graças a função(pegar_segundo_item) que está retornando o segundo item de uma tupla
# aqui temos a mesma lógica onde o parametro key está passando automaticamente a lista de vendas para a função pegar_segundo_item e so depois de receber o valor dessa função ela ordena ele decrescentemente(por conta do reverse = True)

print(dict(lista_vendas)) # aqui estamos retransformando a lista de tuplas em um dicionário ordenado do maior para o menor


# sempre que um parametro ou método aceitar uma function como valor a ser passado, isso ja quer dizer que esse parametro ou método vai pegar essa function e rodar ela pra cada objeto do meu iterable(assim como map)

'''

'''
Lambda expressions
É um função que não tem um nome definido(também chamada de função anÔnima), que executa apenas uma linha de código e são atribuídas a uma variável, como se a variável virasse a função

# estrutura
variável = lambda parametro: expressão

Como se fosse uma função assim:

def minha_funcao(num):
    return num * 2

escrita em apenas uma linha de código e que deve ser atribuída a uma variável(pois a variável vai se tornar a função, que deverá ser chamada para passar os argumentos a ela)

Essa mesma função em lambda expression seria: 

minha_funcao = lambda num: num * 2

print(minha_funcao(10))

a grande sacada do lambda expresion é poder criar funções curtas e rapidas, sem precisar ter de defini-la antes

# vamos usar lambda expressions para criar um função que calcula o preço dos produtos acrescido do imposto

preco = lambda produto: produto * 1.3

print(preco(1000))
'''



'''
Principal aplicação de Lambda expressions

Usar lambda como argumento de alguma outra função, como map e filter

# No map

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

# fazendo com função criada antes
def calcular_imposto(valor):
    return valor * 1.3

preco_com_imposto = list(map(calcular_imposto, preco_tecnologia.values()))

print(preco_com_imposto)

# fazendo com lambda expression

preco_com_imposto = list(map(lambda preco: preco * 1.3, preco_tecnologia.values()))

print(preco_com_imposto)

# basicamente o que esta acontecendo acima é pra cada valor do meu dicionário (preco_tecnologia) eu estou adicionando o mesmo valor + 30 % de imposto, primeiramente utilizando o map com uma função criada previamente(onde o map vai aplicar esse função para calcular o imposto em cada valor do meu dicionario.values()), e depois usando o map com uma expressão lambda (aonde cada valor do meu dicionario.values será mudado atraves da expressão contida na estrutura da lambda( que nesse caso é receber um preco e retornar ele com 30% de imposto)). E ao final de tudo transformamos o objeto map criado em uma lista, para poder ser visível o que aconteceu nisso tudo.

'''


'''
# No filter
Basicamente a função filter é uma função map que aplica um filtro(função que deve retornar True or False) em todos os objetos de um iterable passado para ela

Estrutura
filter(função(de True or False), iterable) -> Retorna como resposta todos os items do iterable onde a função  retornar True como resposta


# Pegando todos os dispositivos que são acima de 2000
'''

preco_tecnologia = {'notebook asus': 2450, 'iphone': 4500, 'samsung galaxy': 3000, 'tv samsung': 1000, 'ps5': 3000, 'tablet': 1000, 'notebook dell': 3000, 'ipad': 3000, 'tv philco': 800, 'notebook hp': 1700}

'''
# fazendo com function
def ta_acima(item):
    return item[1] > 2000

acima_dois_mil = list(filter(ta_acima, preco_tecnologia.items()))

print(acima_dois_mil)

# fazendo com lambda expression

acima_dois_mil = dict(filter(lambda item: item[1] > 2000, preco_tecnologia.items()))

print(acima_dois_mil)

# OBS: O map faz um conta/operação(sem ser lógica), já o filter faz uma comparação que precisa retornar True or False
# OBS2: Case queira trasnformar os objetos tipo map ou filter em dict, tuple, list or set é possível, Assim como eu ja vinha fazendo acima transformando eles sempre em list
# Sempre que sua função puder ser resumida em uma linha, ela pode se transformar em uma lambda expression
'''



'''
Lambda Expressions para gerar funções
# usando o lambda expression dentro da definição de um outra função

Exemplo: Criando uma função que me permita calcular o valor acrescido do imposto de diferentes categorias(produto, serviço, royalties)
# Criando uma função construtora de funções
'''

def calcular_imposto(imposto):
    return lambda preco: preco * (1 + imposto)
# a função acima tem que receber um imposto(preferencialmente em float) pra poder retornar uma função com esse imposto ja embutido(expressão lambda nesse caso, que transformara quem a receber(variavel) em uma função), que tem como parametro a ser passado um preco para ser calculado o novo preço baseado no imposto

# produto 0.1
# serviço 0.14
# royalties 0.24

calcular_preco_produto = calcular_imposto(0.1)
calcular_preco_servico = calcular_imposto(0.14)
calcular_preco_royalties = calcular_imposto(0.24)
# as 3 "variáveis" acima se transformaram em uma função (graças a expressão lambda retornada pela função calcular_imposto()) que recebe como parametro um preço e retorna esse preço + o imposto embutido em cada função graças a função que a gerou(que foi calcular_imposto() com o imposto passado como parametro)

print(calcular_preco_produto(1000))
print(calcular_preco_servico(1000))
print(calcular_preco_royalties(1000))

#OBS: Quando uma função te da como resposta(retorna) um lambda ela na verdade é uma construtora de funções


