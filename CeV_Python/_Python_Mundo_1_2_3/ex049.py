from os import system
system('cls')

print('-=-' * 10 , 'TABUADA LEGAL', '-=-' * 10)

num = int(input('Digite que número você quer saber a tabuada: '))

for i in range(1,11):
    print(f'{num} x {i} = {num * i}')
