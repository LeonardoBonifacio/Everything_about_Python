def somaImposto(taxaImposto,custo):
    novo_custo = custo + (taxaImposto/100 * custo)
    return novo_custo

novo_valor = somaImposto(float(input('Digite a taxa de porcentagem do imposto sobre o produto: ')),float(input('Digite o valor do produto R$')))
print(f'Com essa taxa de imposto o novo valor do produto fica {novo_valor:>.2f}')