'''
Utizizando bibliotecas

import biblioteca = para importar todas as funcionalidades da biblioteca

from biblioteca import x = para importar uma funcionalidade especifica da biblioteca, podendo usar virgulas apos cada funcionalidade para importar mais de uma funcionalidade.

Ao importar funções especificas não há necessidade de dizer de qual biblioteca ela veio antes da variavel e sim so colocar a função(variavel)

As bibliotecas podem ser usadas ainda para formatar variaveis dentro de fstring:
{biblioteca.funcionalidade(variavel)} 
ou 
{funcionalidade(variavel)}

'''
from os import system
system('cls')
from math import sqrt,floor 
num = int(input('Digite um número: '))
raiz = sqrt(num)

print(f'A raiz quadrada de {num} é {floor(raiz):.2f}.')  