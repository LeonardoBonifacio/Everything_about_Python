from os import system
system('cls')

print('__________JoKenPo Ladrão__________')

pedra_papel_tesoura = input('[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n->')

if(pedra_papel_tesoura == '1' ):
    print('Eu escolhi papel e você pedra , ganhei kkkkkkkkkkkkkk.')
elif(pedra_papel_tesoura == '2'):
    print('Eu escolhi Tesoura e você papel , ganhei kkkkkkkkkkkk.')
elif(pedra_papel_tesoura == '3'):
    print('Eu escolhi Pedra e você tesoura, ganhei kkkkkkkkkkkkk.')
else:
    print('Você não escolheu nenhuma opção.')