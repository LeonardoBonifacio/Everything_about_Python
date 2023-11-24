from os import system
system('cls')

print('-=--=--=-CADEIRA PREFERENCIAL-=--=--=-')

preferencial = str(input('Digite [Idoso],[Gestante[,[cadeirante] ou nada: ')).strip().upper()

if(preferencial != 'IDOSO' and preferencial != 'GESTANTE' and preferencial != 'CADEIRANTE'):
    print('Você digitou um valor inválido ou não tem direito a cadeira preferencial')
else:
    print('Você tem direito a cadeira preferencial')
    