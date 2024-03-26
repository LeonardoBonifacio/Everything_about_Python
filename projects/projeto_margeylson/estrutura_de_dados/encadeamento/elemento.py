class Elemento:
    def __init__(self, valor, ligacao=None):
        self.valor = valor
        self.ligacao = ligacao
    
    def __str__(self) -> str:
        return f'{self.valor}'

    def retornaLigacao(self):
        return self.ligacao

    def ligaCom(self, ligacao):
        self.ligacao = ligacao
        