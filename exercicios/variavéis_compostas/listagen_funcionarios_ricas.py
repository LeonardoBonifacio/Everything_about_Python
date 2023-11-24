from os import system
system('cls')

nomes = list()
sexos = list()
salarios = list()

for funcionarios in range(5):
    nomes.append(str(input(f'Digite o nome do {funcionarios + 1}° funcionário: ')))
    sexos.append(str(input(f'Digite o sexo do {funcionarios + 1}° funcionário, [M]asculino ou [F]eminino >>> ')))
    salarios.append(float(input(f'Digite o salário do {funcionarios + 1}° funcionário R$')))
print(f'Listagem das funcionárias que ganham mais de R$5000')
for pos,sexo in enumerate(sexos):
    if(sexo.strip().upper()[0] == 'F' and salarios[pos] > 5000):
        print(f'Funcionário: {nomes[pos]}\nSexo: Feminino\nSalário: R${salarios[pos]}')