from os import system
system('cls')

def leiaInt(msg):
    while(True):
        try:
            n = int(input(msg))
        except (TypeError,ValueError):
            print(f"ERRO: POR FAVOR DIGITE UM NÚMERO INTEIRO.")
        except KeyboardInterrupt:
            print('O usário preferiu não digitar esse número.')
            return 0
        else:
            return n 


def leiaFloat(msg):
    while(True):
        try:
            f = float(input(msg))
        except (TypeError,ValueError):
            print('ERRO: POR FAVOR DIGITE UM NÚMERO REAL')
        except KeyboardInterrupt:
            print("O usuário preferiu não digitar esse número")
            return 0
        else:
            return f


num_int = leiaInt("Digite um numero inteiro: ")

num_float = leiaFloat('Digite um número real (EX: 3.2): ')

print()

print(f'O valor inteiro digitado foi {num_int} e o real foi {num_float}')


