from os import system
system('cls')

def valorPagamento(valor_prestacao,dias_em_atraso):
    global total_pres,qtd_presta
    if(dias_em_atraso == 0):
        print(f'Já que não houve dias em atrasos sua prestação continua em R${valor_prestacao:.2f}')
        total_pres += valor_prestacao
        qtd_presta += 1
    else:
        novo_valor = valor_prestacao + (3/100 * valor_prestacao) + ((0.01 *  dias_em_atraso) * valor_prestacao)
        total_pres += novo_valor
        qtd_presta += 1
        print(f'Por atrasar {dias_em_atraso} o novo valor da prestação ficou em {novo_valor:.2f}')


total_pres = qtd_presta = 0
while(True):
    prestacao = float(input('Digite o valor da prestação(ou 0 para mostrar o relatório) R$'))
    if(prestacao == 0):
        break
    atrasado_a_dias = int(input('Está atrasada a quantos dias essa prestação? '))
    valorPagamento(prestacao,atrasado_a_dias)
print('-' * 20,'Relatório','-' * 20)
print(f'Quantidade de prestações: {qtd_presta}')
print(f'Valor total das prestações: R${total_pres:.2f}')

