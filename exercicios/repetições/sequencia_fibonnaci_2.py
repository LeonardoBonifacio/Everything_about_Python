from os import system
system('cls')

primeiro = 0
segundo = 1
print(primeiro,end = ' ')
print(segundo,end = ' ')
for termos in range(8):
    proximo = primeiro + segundo
    print(proximo,end = ' ')
    primeiro = segundo
    segundo = proximo