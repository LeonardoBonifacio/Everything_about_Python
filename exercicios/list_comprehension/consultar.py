'''

estrutura e exemplos
lista = [expressão for item in iterable]

precos = [100, 140, 300, 7700]
imposto = [preco * 0.3 for preco in precos]


# com uma def dentro da expressão

def calcular_imposto(preco, imposto):
    return preco * imposto

impostos = [calcular_imposto(preco, 0.3) for preco in preco_produtos]

'''

'''
# ordenando(do maior para o menor) duas lista relacionadas
vendas_produtos = [1499, 149, 2100, 1949]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

relacao = [(venda, produto) for venda, produto in zip(vendas_produtos, produtos)]
relacao.sort(reverse=True) # ao chamar o .sort ele vai olhar o primeiro item de cada tupla/lista/dict por padrão
print(relacao)

produtos = [produto for venda, produto in relacao]
print(produtos)
'''


'''
usando o list comprehension para filtra um lista com if
lista  = [expressao for item in iterable if condição]

# digamos que eu queria criar uma lista de produtos que bateram a meta

meta = 1000
vendas_produtos = [1499, 149, 2100, 1949]
produtos = ['vinho', 'cafeteira', 'microondas', 'iphone']

bateram_meta = [(venda,produto) for venda,produto in zip(vendas_produtos, produtos) if venda >= meta]
print(sorted(bateram_meta))

clientes_devedores = [('321.921.402-41', 14404, 24), ('241.479.170-81', 17027, 1), ('297.781.479-21', 8177, 28), ('194.124.842-24', 10000, 19)]

clientes_inadimplentes = [cpf for cpf,valor, dias in clientes_devedores if dias > 20]

print(clientes_inadimplentes)

'''

'''
List comprehension com if para escolher o resultado final
estrutura:  lista = [item if condição else outro_resultado for item in iterable]

vendedores_dict = {'maria': 1200, 'jose': 300, 'antonio': 800, 'joao': 1499, 'francisco': 1900, 'ana': 2749, 'luiz': 400, 'leonardo': 10000}
meta = 1000
bonus_vendedores = [vendas * 0.1 if vendas >= meta else 0 for vendas in vendedores_dict.values()]
print(bonus_vendedores)
'''



'''
Tamanho do pedido de compras

estoque = [('BSA2199',396),('PPF5239',251),('BSA1212',989),('PPF2154',449),('BEB3410',241),('PPF8999',527),('EMB9591',601),('BSA2006',314),('EMB3604',469),('EMB2070',733),('PPF9018',339),('PPF1468',906),('BSA5819',291),('PPF8666',850),('BEB2983',353),('BEB5877',456),('PPF5008',963),('PPF3877',185),('PPF7321',163),('BSA8833',644),('PPF4980',421),('PPF3063',757),('BSA2089',271),('BSA8398',180),('EMB4622',515),('EMB9814',563),('PPF3784',229),('PPF2398',270),('BEB3211',181),('PPF8655',459),('PPF1874',799),('PPF8789',126),('PPF6324',375),('EMB9290',883),('BSA5516',555),('BSA8451',243),('BSA8213',423)]

pedido = [(item,1000) if quantidade < 200 else (item, 500) for item,quantidade in estoque]

print(pedido)

'''



'''
List comprehension não serve so pra criar listas

# vamos calcular quantos % das vendas o meu top 5 produtos representa das vendas totais
produtos = ['coca', 'pepsi', 'guarana', 'skol', 'brahma', 'agua', 'del valle', 'dolly', 'red bull', 'cachaça', 'vinho tinto', 'vodka', 'vinho branco', 'tequila', 'champagne', 'gin', 'guaracamp', 'matte', 'leite de castanha', 'leite', 'jurupinga', 'sprite', 'fanta']
vendas = [1200, 300, 800, 1500, 1900, 2750, 400, 20, 23, 70, 90, 80, 1100, 999, 900, 880, 870, 50, 1111, 120, 300, 450, 800]
top5 = ['agua', 'brahma', 'skol', 'coca', 'leite de castanha']

# fazendo com for
porcentagem = []
total_top5 = 0
for produto, venda in zip(produtos, vendas):
    if produto in top5:
        total_top5 += venda
        porcentagem.append(venda/sum(vendas))

print(f'Top 5 representou {sum(porcentagem):.1%} das vendas')
print(f'Com {total_top5} vendas ao total.')

# fazendo com list comprehension
total_top5 = sum([venda for produto,venda in zip(produtos,vendas) if produto in top5])
print(f'Top 5 representou {(total_top5/sum(vendas)):.2%} das vendas')
print(f'Com {total_top5} vendas ao total.')

'''