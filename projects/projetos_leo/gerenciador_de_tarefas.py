from time import sleep
from os import system
system('cls')
lista_de_tarefas = []
tarefa = {}


def novaTarefa(tituto='Desconhecido', descricao='Sem descrição', prazo='Sem prazo', prioridade='Sem prioridade', situacao='Comecei'):
    try:
        tarefa["Título"] = titulo.title().strip()
        tarefa["Descrição"] = descricao.capitalize().strip()
        tarefa["Prazo"] = prazo.strip()
        tarefa["Prioridade"] = prioridade.title().strip()
        tarefa["Situação"] = situacao.title().strip()
        lista_de_tarefas.append(tarefa.copy())
        tarefa.clear()

    except:
        print('Ocorreu um erro na criação de sua tarefa, por favor tente novamente...')

    else:
        print('Tarefa criada com sucesso')


def listarTarefas(pos=0):
    if (len(lista_de_tarefas) == 0):
        print('Não há nenhuma tarefa cadastrada')
    if (pos != 0):
        for tarefa in lista_de_tarefas[pos]:
            print(f'Titulo: {tarefa["Título"]}')
            print(f'Descrição: {tarefa["Descrição"]}')
            print(f'Prazo: {tarefa["Prazo"]}')
            print(f'Prioridade: {tarefa["Prioridade"]}')
            print(f'Situação: {tarefa["Situação"]}')
            print('-=-' * 18)
    else:
        for tarefa in lista_de_tarefas:
            print(f'Titulo: {tarefa["Título"]}')
            print(f'Descrição: {tarefa["Descrição"]}')
            print(f'Prazo: {tarefa["Prazo"]}')
            print(f'Prioridade: {tarefa["Prioridade"]}')
            print(f'Situação: {tarefa["Situação"]}')
            print('-=-' * 18)


def atualizarTarefa():
    nome = input('Por favor digite o título da tarefa que deseja atualizar: ')
    pos = pesquisarTarefa(nome)
    qtd_alterações = 0
    if (pos != None):
        print('Digite o que você quer atualizar ou deixe em branco caso queira deixar como esta')
        novo_t = input("Novo título: ").title().strip()
        if (novo_t != ""):
            lista_de_tarefas[pos]["Título"] = novo_t
            print('Título alterado com sucesso')
            qtd_alterações += 1
        while (True):
            nova_d = input('Nova descrição: ').capitalize().strip()
            if (len(nova_d) > 100):
                print('Por favor a nova descrição não pode ultrapassar 100 caracteres.')
            else:
                break
        if (nova_d != ""):
            lista_de_tarefas[pos]["Descrição"] = nova_d
            print('Descrição alterada com sucesso')
            qtd_alterações += 1
        while (True):
            mudar_prazo = str(
                input('Deseja mudar o prazo da Tarefa? [S/N]')).upper().strip()[0]
            if (mudar_prazo in "SN"):
                break
        if (mudar_prazo == 'S'):
            while (True):
                novo_p = str(
                    input('Novo Prazo da Tarefa[xx/xx/xxxx]:')).strip()
                if ('/' not in novo_p):
                    print('Por favor digite o prazo com "/"(Ex: 10/11/2023)')
                elif (int(novo_p[0:2]) < 1 or int(novo_p[0:2]) > 31):
                    print('Por favor digite um dia entre 1 e 31')
                elif (int(novo_p[3:5]) < 1 or int(novo_p[3:5]) > 12):
                    print('Por favor ditite um mês válido(entre 1 e 12)')
                elif (len(novo_p[-4:]) != 4):
                    print(
                        'Por favor digite a quantidade de digitos corretos para o ano...')
                else:
                    break
            print('Prazo alterado com sucesso')
            qtd_alterações += 1
        while (True):
            nova_pri = str(
                input('Nova Prioridade da Tarefa[Baixa/Média/Alta]: ')).strip().title()
            if (nova_pri == ''):
                break
            elif (nova_pri.title() not in ['Baixa', 'Média', 'Alta']):
                print(
                    'Por favor, escolha apenas entre esses 3 niveis de prioridade [Baixa/Média/Alta]\nOBS:Não esqueça dos acentos...')
            else:
                qtd_alterações += 1
                print('Prioridade alterada com sucesso')
                break
        while (True):
            novo_sta = str(
                input('Novo Status da Tarefa[Comecei/Fazendo/Terminei]'))
            if (novo_sta == ""):
                break
            elif (novo_sta.title().strip() not in ['Comecei', 'Fazendo', 'Terminei']):
                print(
                    'Por favor, escolha apenas entre esses 3 niveis de status [Comecei/Fazendo/Alta]')
            else:
                qtd_alterações += 1
                print('Status alterado com sucesso')
                break
        print(f'Você fez {qtd_alterações} alterações nessa tarefa.')


def removerTarefa():
    nome = input("Digite o nome da tarefa que deseja excluir: ")
    pos = pesquisarTarefa(nome)
    if (pos != None):
        while (True):
            decisao = input(
                'Tem certeza que deseja excluir essa tarefa? [S/N]').strip().upper()[0]
            if (decisao in "SN"):
                break
        if (decisao == 'S'):
            print('OK Excluindo tarefa...', flush=True)
            sleep(3)
            del lista_de_tarefas[pos]
            print('Tarefa excluída com sucesso')
        else:
            print("Pense sempre duas vezes ao excluir algum dado, volte sempre...")


def filtrarTarefasPrioridade(priori):
    nao_tem_prioridade = 0
    for tarefa in lista_de_tarefas:
        if (tarefa["Prioridade"] == priori):
            print(f'Titulo: {tarefa["Título"]}')
            print(f'Descrição: {tarefa["Descrição"]}')
            print(f'Prazo: {tarefa["Prazo"]}')
            print(f'Prioridade: {tarefa["Prioridade"]}')
            print(f'Situação: {tarefa["Situação"]}')
            print('-=-' * 18)
        else:
            nao_tem_prioridade += 1
    if (len(lista_de_tarefas) == nao_tem_prioridade):
        print('Não existe nenhuma tarefa com essa prioridade')


def pesquisarTarefa(title):
    cont = 0
    for tarefa in lista_de_tarefas:
        if (tarefa["Título"] == title):
            pos = lista_de_tarefas.index(tarefa)
            listarTarefas(pos)
        else:
            cont += 1
    if (cont == len(lista_de_tarefas)):
        print('Tarefa não encontrada ou nome imcompatível')
    else:
        print('Tarefa encontrada com sucesso!')
        return pos


def limparTela():
    system('cls')


def pausar():
    input('Tecle [ENTER] para continuar')


while (True):
    limparTela()
    print('=' * 20, 'GERENCIADOR DE TAREFAS', '=' * 20)
    menu = str(input('[1] - Nova Tarefa\n[2] - Listar Tarefas\n[3] - Atualizar Tarefa\n[4] - Remover Tarefa\n[5] - Filtrar tarefas por prioridade\n[6] - Pesquisar Tarefa\n[0] - Finalizar Gerenciador\n>>> '))

    if (menu == '1'):
        limparTela()
        print('-' * 40)
        print("CRIANDO TAREFA".center(40))
        print('-' * 40)
        titulo = str(input('Título da tarefa: ')).strip().title()
        while (True):
            descricao = str(
                input('Descrição da tarefa (no máximo 100 caracteres):')).strip().title()
            if (len(descricao) > 100):
                print("Por favor digite uma descrição com no máximo 100 caracteres.")
            else:
                break
        while (True):
            prazo = str(input('Prazo da Tarefa[xx/xx/xxxx]:')).strip()
            if ('/' not in prazo):
                print('Por favor digite o prazo com "/"(Ex: 10/11/2023)')
            elif (int(prazo[0:2]) < 1 or int(prazo[0:2]) > 31):
                print('Por favor digite um dia entre 1 e 31')
            elif (int(prazo[3:5]) < 1 or int(prazo[3:5]) > 12):
                print('Por favor ditite um mês válido(entre 1 e 12)')
            elif (len(prazo) != 10):
                print('Por favor digite a quantidade de digitos corretos para a data...')
            else:
                break
        while (True):
            prioridade = str(
                input('Prioridade da Tarefa[Baixa/Média/Alta]: ')).strip().title()
            if (prioridade.title() not in ['Baixa', 'Média', 'Alta']):
                print(
                    'Por favor, escolha apenas entre esses 3 niveis de prioridade [Baixa/Média/Alta]\nOBS:Não esqueça dos acentos...')
            else:
                break
        while (True):
            status = str(input('Status da Tarefa[Comecei/Fazendo/Terminei]'))
            if (status.title().strip() not in ['Comecei', 'Fazendo', 'Terminei']):
                print(
                    'Por favor, escolha apenas entre esses 3 niveis de status [Comecei/Fazendo/Alta]')
            else:
                break
        novaTarefa(titulo, descricao, prazo, prioridade, status)
        pausar()
    elif (menu == '2'):
        limparTela()
        print('-' * 40)
        print('LISTANDO SUAS TAREFAS'.center(40))
        print('-' * 40)
        listarTarefas()
        pausar()
    elif (menu == '3'):
        limparTela()
        print('-' * 40)
        print('ATUALIZANDO TAREFAS'.center(40))
        print('-' * 40)
        atualizarTarefa()
        pausar()
    elif (menu == '4'):
        limparTela()
        print('-' * 40)
        print('EXCLUINDO TAREFA'.center(40))
        print('-' * 40)
        removerTarefa()
        pausar()
    elif (menu == '5'):
        limparTela()
        print('-' * 40)
        print('FILTRANDO TAREFAS'.center(40))
        print('-' * 40)
        while (True):
            prioridade = input(
                'Digite por qual prioridade você quer filtrar suas tarefas [BAIXA/MÉDIA/ALTA]: ').strip().title()
            if (prioridade not in ['Baixa', 'Média', 'Alta']):
                print(
                    'Por favor escolha somente esses 3 níveis de prioridade [Baixa/Média/Alta]\nOBS:Não esqueça dos acentos...')
            else:
                break
        filtrarTarefasPrioridade(prioridade)
        pausar()
    elif (menu == '6'):
        limparTela()
        print('-' * 40)
        print('PESQUISANDO TAREFA'.center(40))
        print('-' * 40)
        nome = str(
            input('Digite o título da tarefa que deseja pesquisar: ')).strip().title()
        pesquisarTarefa(nome)
        pausar()
    elif (menu == '0'):
        break
    else:
        input('Opção inválida, por favor tecle [ENTER] para continuar.')
        limparTela()
print('Gerenciador de tarefas finalizado com sucesso\nPor favor volte sempre que precisar...')
