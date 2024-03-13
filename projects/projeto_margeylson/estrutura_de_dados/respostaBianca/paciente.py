class Paciente:

    def __init__(self, nome, situacao):
        self.nome = nome
        self.situacao = situacao

    def __str__(self):
        return f'Paciente: {self.nome}. Situação: {self.situacao}'
    