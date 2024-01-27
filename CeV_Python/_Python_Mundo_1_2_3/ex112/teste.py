from utilidadesCeV import moeda, dado
from os import system
system('cls')
p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 20, 12)
