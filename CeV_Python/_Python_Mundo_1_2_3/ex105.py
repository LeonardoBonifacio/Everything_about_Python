from os import system
system('cls')


def notas(*notas,sit = False):
    """
    -> Função para anaisar notas e sitações de vários alunos.
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a sitação
    :return: dicionário com várias informaões sobre a sitação da turma.
    """
    dicio_notas = {}
    dicio_notas["Total"] = len(notas)
    dicio_notas["Maior"] = max(notas)
    dicio_notas["Menor"] = min(notas)
    dicio_notas["Média"] = sum(notas)/(len(notas))
    if(sit == True):
        if(dicio_notas["Média"] <= 4):
            dicio_notas["Situação"] = "PÉSSIMA"
        elif(dicio_notas["Média"] <= 7):
            dicio_notas["Situação"] = "RAZOÁVEL"
        else:
            dicio_notas["Situação"] = "BEM BOA"
    return dicio_notas

resp = notas(7,8,9,3,4,sit=True)
print(resp)
help(notas)
