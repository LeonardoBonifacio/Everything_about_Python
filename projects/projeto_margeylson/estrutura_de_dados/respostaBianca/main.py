import os
from paciente import Paciente
from fila_comum import FilaComum
from fila_prioridade import FilaPrioridade
from fila_emergencia import FilaEmergencia

comum = FilaComum()
prioritaria = FilaPrioridade()
emergencia = FilaEmergencia()

contador_emergencia = 0
contador_prioritaria = 0
contador_comum = 0


def limpar_tela():
    os.system('cls')


def adicionar_paciente():
    nome = input("Nome: ")
    print("Situação do paciente")
    print("[1] - Verde (situação geral)")
    print("[2] - Amarelo (60 anos, com gestantes lactantes e PCD)")
    print("[3] - Vermelho (situação de urgência)")
    op = int(input("> "))
    paciente_novo = Paciente(nome, op)
    if op == 1:
        comum.enqueue(paciente_novo)
    elif op == 2:
        prioritaria.enqueue(paciente_novo)
    elif op == 3:
        emergencia.enqueue(paciente_novo)
    else:
        print("Opção inválida")


def proximo_fila():
    global contador_prioritaria
    global contador_emergencia
    global contador_comum
    
    if not emergencia.is_empty() and contador_emergencia < 2:
        emergencia.dequeue()
        contador_emergencia += 1
        print(contador_emergencia)
        input("ENTER")
    elif not prioritaria.is_empty() and contador_prioritaria < 3:
        prioritaria.dequeue()
        contador_prioritaria += 1
        print(contador_prioritaria)
        input("ENTER")
    else:
        comum.dequeue()
        contador_comum += 1
        print(contador_comum)
        input("ENTER")

    if contador_comum > 0 and contador_prioritaria > 0 and contador_emergencia > 0:
        contador_emergencia = 0
        contador_prioritaria = 0
        contador_comum = 0


def visualizar_filas():
    limpar_tela()
    print("Fila Comum")
    comum.visualizar_fila()
    print("=" * 40)

    print("Fila Prioritária")
    prioritaria.visualizar_fila()
    print("=" * 40)
    
    print("Fila Emergencial")
    emergencia.visualizar_fila()
    print("=" * 40)
    input("ENTER")

def main():
    while True:
        limpar_tela()

        print("MENU")
        print("[1] - Adicionar Paciente")
        print("[2] - Iniciar Atendimento")
        print("[3] - Visualizar Filas")
        print("[0] - Sair")
        print("=" * 40)
        op = int(input(">> "))

        if op == 1:
            limpar_tela()
            print("Adicionar")
            adicionar_paciente()
        elif op == 2:
            limpar_tela()
            print("Iniciando atendimento")
            proximo_fila()
        elif op == 3:
            limpar_tela()
            print("Visualizar Filas")
            visualizar_filas()
        elif op == 0:
            limpar_tela()
            print("Sair")
            break
        else:
            print("Insira uma opção válida")


main() 
