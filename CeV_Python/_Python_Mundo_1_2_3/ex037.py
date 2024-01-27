from os import system
system('cls')

print('-=-' * 12, 'CONVERTENDO BASES NÚMERICAS' ,'-=-' * 12)

num = int(input('Digite um número \033[1minteiro\033[m: '))
conversao_base = int(input('[1] - Converter en binário\n[2] - Converter em octal\n[3] - Converter em hexadecimal\n-> '))

if(conversao_base == 1):
    print(f'O número {num} em binário é {num:0b}') #:0b para converter para binário
elif(conversao_base == 2):
    print(f'O número {num} em octal é {num:0o}') #:0o para converter para octal
elif(conversao_base == 3):
    print(f'O número {num} em hexadecimal é {num:0x}') #:0x para converter para hexadecimal
else:
    print('Valor inválido.')

#Posso fazer desse jeito ai tbm
#print(oct(num)[2:])
#print(hex(num)[2:])      
#print(bin(num)[2:])
