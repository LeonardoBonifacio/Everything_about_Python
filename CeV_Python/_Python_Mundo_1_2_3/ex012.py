preco_produto = float(input('Digite o preço do produto que você deseja comprar? R$'))
novo_preco = preco_produto - (preco_produto * (5/100))
desconto = preco_produto * (5/100)
print(f'Por algum motivo aleatorio você ganhou um desconto de R${desconto:.2f} (5% de desconto) o novo valor que você irá pagar é de R${novo_preco:.2f}.')