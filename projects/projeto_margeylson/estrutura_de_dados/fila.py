# Fila.py
class Fila:
    def __init__(self):
        self.roteiro = []
    
    def estaVazia(self):
        check = False
        if len(self.roteiro == 0):
            check = True
        return check
    
    def addParada(self, cidade):
        self.roteiro.append(cidade)
    
    def removerCidade(self):
        if not self.estaVazia():
            print(f"Removendo {self.roteiro[0]}")
            del self.roteiro[0]
    

    def visualizarRoteiro(self):
        if not self.estaVazia():
            for cidade in self.roteiro:
                print(cidade)