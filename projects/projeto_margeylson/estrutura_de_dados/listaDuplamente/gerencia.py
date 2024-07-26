from elemento import Elemento
from pedido import Pedido
import os


# Exiba os pedidos, bem como seus detalhes, do primeiro ao último
# Exiba os valores do último ao primeiro
# Exiba o valor total de todos os pedidos feito.
# Extra: Prove que é bom --> Exiba o total dos pedidos por tipo de pagamento.
# Seu programa encerra ao digitar FIM na entrada de pedidos

primeiro = ultimo = None
listaItens = []
nomeCliente = enderecoEntrega = formaPagamento = ""
while True:
    while True:
        print("========== MENU DA LANCHONETE ==========")
        print("[1]  Pastel com caldo de cana               -> R$15")
        print("[2]  Coxinha de catupiri com suco de goiaba -> R$12")
        print("[3]  Fatia de pizza universal com Coca      -> R$17")
        print("[4]  Pamonha com mingau de milho            -> R$14")
        print("[5]  Tapioca de quejunto e preso            -> R$10")
        print("[6]  Bolo de pote de doce de leite          -> R$14")
        print("[7]  Palha italiana de ninho                -> R$10")
        print("[8]  Caldo de feijão                        -> R$12")
        print("[9]  Canjica de milho                       -> R$13")
        print("[10] Empadão de frango                      -> R$25")
        print("[0]  Encerrar este pedido")
        item = int(input('->  '))
        if item in Pedido.itensMenu:
            listaItens.append(item)
            os.system("cls")
        else:
            break

    if item == 0:
        os.system("cls")
        print("========== Coletando seus dados ==========")
        nomeCliente = input("Digite seu nome: ").strip().capitalize()
        enderecoEntrega = input("Digite seu endereço de entrega: ").strip()
        formaPagamento = input("Será PIX, DINHEIRO, DÉBITO ou CRÉDITO? ").upper().strip()
        
        pedido = Pedido(listaItens,nomeCliente,enderecoEntrega,formaPagamento)
        novo = Elemento(pedido)
        if primeiro == None:
            primeiro = novo
            ultimo = novo
        else:
            ultimo.define_proximo(novo)
            novo.define_anterior(ultimo)
            ultimo = novo
    resp = input('Deseja fazer outro pedido?[S/N]').strip().upper()[0]
    if resp != "S":
        break
    listaItens.clear()


while True:
    print("========== MENU DA LISTA DUPLAMENTE ENCADEADA =========")
    print("[1] - Exibir do primeiro ao último pedido ")
    print("[2] - Exibir do último ao primeiro pedido")
    print("[3] - Exibir valor total de todos os pedidos feitos ")
    print("[0] - Encerrar programa ")
    op = input("-> ")
    if op == "1":
        os.system("cls")
        aux = primeiro
        while aux:
            aux.valor.descreverPedido()
            aux = aux.retorna_proximo()
    elif op == "2":
        os.system("cls")
        aux = ultimo
        while aux:
            aux.valor.descreverPedido()
            aux = aux.retorna_anterior()
    elif op == "3":
        os.system("cls")
        aux = primeiro
        valorTotal = 0
        while aux:
            valorTotal += aux.valor.valorTotalPedido
            aux = aux.retorna_proximo()
        print(f"O valor total de todos os pedidos foi de R$ {valorTotal}")
    else:
        print("CABOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
        break