from os import system
system('cls')
sexo = 'v'
while(sexo not in 'M F'):
    sexo = str(input('Sexo: [M]asculino ou [F]eminino\n>>> ')).strip().upper()[0]
    if(sexo != 'F' and sexo != 'M'):
        print('Sexo inválido, tente novamente')
        input('[ENTER] - Para continuar')
        system('cls')
print('Parabens por conseguir digitar seu sexo...')