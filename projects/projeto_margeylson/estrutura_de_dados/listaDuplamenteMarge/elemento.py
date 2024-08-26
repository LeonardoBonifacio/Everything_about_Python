class Elemento:

    def __init__(self, valor, proximo=None, anterior=None):
        self.valor = valor
        self.proximo = proximo
        self.anterior = anterior
    
    
    def __str__(self):
        return f'<== {self.valor} ==> '
    
    
    def defineProximo(self, proximo):
        self.proximo = proximo
   
    
    def defineAnterior(self, anterior):
        self.anterior = anterior
        
        
    def retornaProximo(self):
        return self.proximo
    
        
    def retornaAnterior(self):
        return self.anterior