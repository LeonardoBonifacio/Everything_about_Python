from os import system
system('cls')

print('----------GANHANDO DESCONTOS NA SARAIVA----------')

profissao = int(input('Profissão: \n[1] - Sou professor\n[2] - Não sou professor\n->  '))

if(profissao == 1):
    print('Você ganhou um desconto de 20% por ser professor')
    esfera = int(input('Digite em que esfera de trabalho se encontra: \n[1] - Federal\n[2] - Estadual\n[3] - Municipal\n->  '))
    if(esfera == 1 and profissao == 1):
        print('Por ser professor e atuar na esfera federal você ganhou 30% de desconto na livraria saraiva.')
    else:
        print('Você não ganhou mais 10% de desconto por ser da esfera federal.')
else:
    print('Você não ganhou nenhum desconto, somente professores ganham desconto.')   