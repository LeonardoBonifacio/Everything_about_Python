from os import system
system('cls')

print('__________TROCANDO HORAS DE EXERCÍCIO POR DINDIN__________')

horas_exercicio_mes = int(input('Por quantas horas no ultimo mês você praticou atividades fisicas: '))

if(horas_exercicio_mes > 0 and horas_exercicio_mes <= 10):
    pontos = 2 * horas_exercicio_mes
    ganhos_por_pontos = pontos * 0.05
    print(f'Já que você se exercitou por {horas_exercicio_mes}h no último mês, você acumulou {pontos} pontos.')
    print(f'E ganhou R${ganhos_por_pontos:.2f} por esses pontos acumulados.')
elif(horas_exercicio_mes > 10 and horas_exercicio_mes <= 20):
    pontos = 5 * horas_exercicio_mes
    ganhos_por_pontos = pontos * 0.05
    print(f'Já que você se exercitou por {horas_exercicio_mes}h no último mês, você acumulou {pontos} pontos.')
    print(f'E ganhou R${ganhos_por_pontos:.2f} por esse pontos acumulados.')
elif(horas_exercicio_mes > 20):
    pontos = 10 * horas_exercicio_mes
    ganhos_por_pontos = pontos * 0.05
    print(f'Já que você se exercitou por {horas_exercicio_mes}h no último mês, você acumulou {pontos} pontos.')
    print(f'E ganhou R${ganhos_por_pontos:.2f} por esse pontos acumulados.')
else:
    print(f'Você não ganhou nenhum ponto para trocar por dinheiro , já que o seu número de horas exercicitadas foi de {horas_exercicio_mes}h.')