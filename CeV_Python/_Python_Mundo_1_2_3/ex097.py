from os import system
system('cls')

def escreva(texto):
    tamanho = len(texto)
    print('~' * (tamanho + 2))
    print(f' {texto}')
    print('~' * (tamanho + 2))

escreva('Gustavo Guanabara')
escreva('Curso em Python no Youtube')
escreva('CeV')