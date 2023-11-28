from os import system
system('cls')

def cumprimentaUsuario(nome):
    print(f'Bom dia,{nome}. ')

us = str(input("Digite seu nome: "))
cumprimentaUsuario(us)

