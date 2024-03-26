from os import system
from fila import Fila
from paciente import Paciente

filaComum = Fila()
filaPrioridade = Fila()
filaEmergencia = Fila()

def limpaTela():
    system('cls')

def menu():
    limpaTela()
    print('|============== [ FILA DE PACIENTES ] ===============|')
    print('| [ 1 ] - Adicionar Paciente                         |')
    print('| [ 2 ] - Chamar o Próximo                           |')
    print('| [ 3 ] - Visualizar Fila                            |')
    print('| [ 0 ] - Sair                                       |')
    print('|====================================================|')
    op = input('> ')

    if op == '1':
        limpaTela()
        adicionarPaciente()
    elif op == '2':
        limpaTela()
        chamaProximo()
    elif op == '3':
        limpaTela()
        visualizarFila()
    elif op == '0':
        print('Saindo do Sistema.')
        return -1
    else:
        input('Opção inválida! [ENTER]')


def adicionarPaciente():
    print(' >>>>>>>>>>>>>>>>>> ADICIONAR PACIENTE\n')

    nome = input('Nome do paciente: ')
    while True:
        print('[C]omum | [P]rioridade | [E]mergência')
        categoria = input('>')[0].upper()
        if categoria in ['C', 'P', 'E']:
            break
    
    novoPaciente = Paciente(nome, categoria)
    if novoPaciente.categoria == 'C':
        filaComum.adicionaPaciente(novoPaciente)
    elif novoPaciente.categoria == 'P':
        filaPrioridade.adicionaPaciente(novoPaciente)
    else:
        filaEmergencia.adicionaPaciente(novoPaciente)
    
    input('Paciente adiconado com sucesso! [ENTER]')


def chamaComum():
    print(f'COMUM: {filaComum.chamaProximo()}')
    input('[ENTER]')

def chamaPrioridade():
    print(f'PRIORIDADE: {filaPrioridade.chamaProximo()}')
    input('[ENTER]')

def chamaEmergencia():
    print(f'EMERGÊNCIA: {filaEmergencia.chamaProximo()}')
    input('[ENTER]')

contadorChamada = 0
def chamaProximo():
    global contadorChamada

    if filaEmergencia.tamanhoDaFila() > 0 and contadorChamada < 2:
        chamaEmergencia()
        contadorChamada += 1

    elif filaPrioridade.tamanhoDaFila() > 0 and contadorChamada < 6:
        chamaPrioridade()
        contadorChamada += 1
    
    elif filaComum.tamanhoDaFila() > 0 and contadorChamada < 8:
        chamaComum()
        contadorChamada = 0
    
    else:
        input('Não há pacientes na fila!')


def visualizarFila():
    print('==== [ EMERGÊNCIAS ] =========================')
    filaEmergencia.visualizarFila()
    print('\n')

    print('==== [ PRIORIDADES ] =========================')
    filaPrioridade.visualizarFila()
    print('\n')

    print('==== [ COMUM ] =========================')
    filaComum.visualizarFila()
    print('\n')

    input('[ENTER] para continuar...')


#============== principal
while True:
    if menu() == -1:
        break