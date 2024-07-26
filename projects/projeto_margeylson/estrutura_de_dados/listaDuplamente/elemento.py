class Elemento:

    def __init__(self, valor, anterior=None, proximo=None):
        self.valor = valor
        self.anterior = anterior
        self.proximo = proximo

    def __str__(self):
        return f'{self.valor}'
    
    def retorna_anterior(self):
        return self.anterior
    
    def retorna_proximo(self):
        return self.proximo
    
    def define_anterior(self, novo_anterior):
        self.anterior = novo_anterior
    
    def define_proximo(self, novo_proximo):
        self.proximo = novo_proximo

    