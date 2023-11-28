from os import system
system('cls')
while(True):
    população_pais_1 = int(input('Digite a população do 1° país: '))
    taxa_crescimento_pais_1 = float(input('Taxa de crescimento 1° país (EX: 3.5 para 3.5%): '))
    população_pais_2 = int(input('Digite a população do 2° pais: '))
    taxa_crescimento_pais_2 = float(input('Taxa de crecimento 2° páis (EX: 4.5 para 4.5%): '))

    if(população_pais_1 > população_pais_2):
        mais_populoso = população_pais_1
        taxa_mais_populoso = taxa_crescimento_pais_1
        menos_populoso = população_pais_2
        taxa_menos_populoso = taxa_crescimento_pais_2
    else:
        mais_populoso = população_pais_2
        taxa_mais_populoso = taxa_crescimento_pais_2
        menos_populoso = população_pais_1
        taxa_menos_populoso = taxa_crescimento_pais_1
    anos = 0
    while(menos_populoso <= mais_populoso):
        anos += 1
        menos_populoso += ((taxa_menos_populoso/100) * menos_populoso)
        mais_populoso += ((taxa_mais_populoso/100) * mais_populoso) 
    print(f'O pais menos populoso passou a ter {menos_populoso:.0f} habitantes\nEnquanto o pais mais populoso passou a ter {mais_populoso:.0f} habitantes nesses {anos} anos')
    continuar = str(input('Deseja verificar outros paises? [S]im ou [N]ão\n>>> ')).strip().upper()[0]
    if(continuar == 'N'):
        break
    system('cls')
print('Verificações concluidas com sucesso\nFIM DO PROGRAMA')
    