import os 
os.system('cls')

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
sub = n1 - n2
di = n1 // n2
ex = n1 ** n2
resto = n1 % n2
print(f'> A soma vale {s}  \n', end = '> ')
print(f'A subtração vale {sub}  \n', end = '> ')
print(f'A multiplicação vale {m}  \n', end = '> ')
print(f'A divisão vale {d:.2f}  \n', end = '> ')
print(f'A divisão inteira vale {di}  \n', end = '> ')
print(f'A exponenciação vale {ex} \n', end = '> ')
print(f'O resto da divisão vale {resto} .')

'''
end = '' para não quebrar a linha ou por algo ao final dos prints
\n para quebrar a linha no meio de algum print
:.número de cadas f (:.3f) para formatar as casas decimais de um número
:, para que apareçam , entre as milhares de um número
os dois comandos acima podem ser mescalhados para que apareçam tanto as casas decimais quanto as casas de milhas.
'''