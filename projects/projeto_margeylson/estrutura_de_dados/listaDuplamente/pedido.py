class Pedido:
    itensMenu = {
            1: ("Pastel com caldo de cana", 15),
            2: ("Coxinha de catupiri com suco de goiaba", 12),
            3: ("Fatia de pizza universal com Coca", 17),
            4: ("Pamonha com mingau de milho", 14),
            5: ("Tapioca de quejunto e preso", 10),
            6: ("Bolo de pote de doce de leite", 14),
            7: ("Palha italiana de ninho", 10),
            8: ("Caldo de feijão", 12),
            9: ("Canjica de milho", 13),
            10: ("Empadão de frango", 25)
        }
    def __init__(self, lista_itens, nome_cliente, endereco_entrega, forma_pagamento):
        self.lista_itens = lista_itens
        self.nome_cliente = nome_cliente
        self.endereco_entrega = endereco_entrega
        self.forma_pagamento = forma_pagamento
        self.lista_valores_itens = [Pedido.itensMenu[item][1] for item in lista_itens]
        self.valorTotalPedido = sum(self.lista_valores_itens)

    def descreverPedido(self):
        print(f"""Informações sobre o pedido 
        Nome Cliente: {self.nome_cliente}
        Endereço Entrega: {self.endereco_entrega}
        Forma pagamento: {self.forma_pagamento}
        Valor total Pedido: R$ {self.valorTotalPedido:.2f}
        Itens do pedido e seus preços: """)
        for i, item in enumerate(self.lista_itens):
            nome_item = Pedido.itensMenu[item][0]
            valor_item = self.lista_valores_itens[i]
            print(f"<====== Item: {nome_item}  Valor R$ {valor_item:.2f}")