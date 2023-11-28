from os import system
system('cls')
tot_pag_homens = 0
tot_pag_mulheres = 0
while(True):
    system('cls')
    salario = float(input('Digite o salário: '))
    sexo = str(input('[M] - Masculino \n[F] - Feminino\n>>> ')).strip().upper()
    continuar = str(input('Quer continuar? [S] ou [N]')).strip().upper()
    if(sexo == 'M'):
        tot_pag_homens += salario
    elif(sexo == 'F'):
        tot_pag_mulheres += salario
    if(continuar == 'N'):
        break
print(f'Foram pagos exatos R${tot_pag_homens:.2f} aos homens')
print(f'Foram pagos exatos R${tot_pag_mulheres:.2f} as mulheres')
