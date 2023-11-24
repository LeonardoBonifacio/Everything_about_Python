frase1 = str(input('Digite uma frase qualquer: '))
frase2 = str(input('Digite no máximo 3 caracteres que estão presentes na frase acima: '))
frase3 = str(input('Digite a mesma quantidade de caracteres digitados acima para sererm trocados paralelamente na 1° frase: '))
frase1_split = list(frase1)
frase2_split = list(frase2)
frase3_split = list(frase3)

for caracteres2,caractere3 in zip(frase2_split,frase3_split):
    while(True):
        frase1_split.insert(frase1_split.index(caracteres2), caractere3)
        frase1_split.remove(caracteres2)
        if(caracteres2 not in frase1_split):
            break
print(''.join(frase1_split))
