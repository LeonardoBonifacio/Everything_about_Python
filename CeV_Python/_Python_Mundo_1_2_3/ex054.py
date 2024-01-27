from os import system
system('cls')
from datetime import date
ja_atingiram_maioridade = 0
nao_atingiram_maioridade = 0
for pessoas in range(1,8):
    ano_nascimento = int(input(f'Ano de nascimento da {pessoas}° pessoa: '))
    idade = date.today().year - ano_nascimento
    if(idade > 21):
        ja_atingiram_maioridade += 1
    else:
        nao_atingiram_maioridade += 1
print(f'Das 7 datas de nascimento informadas:\n{ja_atingiram_maioridade} pessoas já atingiram maior idade\n{nao_atingiram_maioridade} pessoas não atingiram maioridade')