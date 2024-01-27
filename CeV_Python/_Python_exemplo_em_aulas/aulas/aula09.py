frase = 'Curso em Video Python'

dividido = frase.split()

print(dividido[2][3])


print(frase.lower().find('video'))

print('Curso' in frase)

print(frase.replace('Python', 'Android'))
'''So substitui momentaneamente e não salva os resultados,
caso queira que substituia é so atribuir a susbstituição
a variável, por exemplo: frase = frase.replace('Python','Android')'''


print(len(frase.strip()))

print(frase.upper().count('O'))

print(frase.count('o'))

print(frase)
print(frase[1])
print(frase[3:13])
print(frase[4::2])
for letra in frase[::-1]:
    print(letra,end = '')

print('''\nLeo é doido
Leo é doido
completamente doido
''')
# Usar asplas triplas ('''''') tem a mesma função de usar o \n para quebrar a
# linha e escrever sem precisar adicionar mais prints()
