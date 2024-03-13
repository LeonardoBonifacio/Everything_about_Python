# Nome da Cidade
# Distância da Capital
# Quantidade de Alunos

class Cidade:
    def __init__(self, nome, distCapital, qtdAlunos):
        self.cidade = nome
        self.distCapital = distCapital
        self.qtdAlunos = qtdAlunos
    
    def __str__(self):
        return f'Cidade: {self.cidade}. Alunos: {self.qtdAlunos}'