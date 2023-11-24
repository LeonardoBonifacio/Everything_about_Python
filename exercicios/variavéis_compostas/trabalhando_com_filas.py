from os import system
system('cls')

ultimo_fila2 = 10
ultimo_fila1 = 10
fila1 = list(range(1, ultimo_fila1 + 1))
fila2 = list(range(1,ultimo_fila2 + 1))

print('-=' * 30)
print(f'{"GERENCIANDO LISTAS":^60}')
print('-=' * 30) 

while(True):
    print(f'Existem {len(fila1)} clientes na 1° fila')
    print(f'Existem {len(fila2)} clientes na 2° fila')
    print(f'1° fila atual: {fila1}')
    print(f'2° fila atual: {fila2}')
    print(f'Digite F para adicionar um cliente ao fim da  1° fila ou G para adcionard um cliente ao fima da 2° fila\nA para realizar o atendimento na 1° fila ou B para realizar o antendimento na 2° fila. S para Sair.')
    operacao = str(input('Operação (F,G,A,B ou S)')).strip().upper()
    if(operacao.count('A') > 0 or operacao.count('B')):
        for atendimento in range(operacao.count('A')):
            if(len(fila1) > 0):
                atendido = fila1.pop(0)
                print(f'Cliente {atendido} atendido da 1° fila')
            else:
                print('Fila vazia! Ninguém para atender. ')
        for atendimento in range(operacao.count('B')):
            if(len(fila2) > 0):
                atendido = fila2.pop(0)
                print(f'Cliente {atendido} atendido da 2° fila')
            else:
                print('Fila vazia! Ninguém para atender. ')
    if(operacao.count('F') > 0 or operacao.count('G')):
        for adicionar in range(operacao.count('F')):
            ultimo_fila1 += 1
            fila1.append(ultimo_fila1)
            print(f'Cliente {ultimo_fila1} adicionado a 1° fila')
        for adicionar in range(operacao.count('G')):
            ultimo_fila2 += 1
            fila2.append(ultimo_fila2)
            print(f'Cliente {ultimo_fila2} adicionado a 2° fila')
    if(operacao.count('S') > 0):
        break
    if(operacao.count('A') == 0 and operacao.count('F') == 0 and operacao.count('S') == 0 and operacao.count('B') == 0 and operacao.count('G') == 0):
        print('Operação inválida\nPor favor digite A ou B para atender\nF ou G para adicionar alguém as filas\nOu S para finalizar o programa')

    
