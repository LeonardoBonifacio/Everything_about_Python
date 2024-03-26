class Paciente:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
    
    def __str__(self):
        return f'Nome: {self.nome}\nCat: {self.categoria}'
    
    def retornaNome(self):
        return self.nome
        
    def retornaCategoria(self):
        return self.categoria