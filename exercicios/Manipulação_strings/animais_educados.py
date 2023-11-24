from os import system
system('cls')

frase = 'Cachorros são muito educados(as)'

animal = str(input('Digite qualquer animal: ')).strip().title()

print(frase.replace('Cachorros',animal))

#As loucuras de Margeylson