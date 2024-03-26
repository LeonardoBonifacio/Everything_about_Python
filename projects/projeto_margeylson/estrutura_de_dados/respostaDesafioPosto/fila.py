class Fila:
    def __init__(self):
        self.fila = []
    
    def adicionaPaciente(self, paciente):
        self.fila.append(paciente)
    
    def removePaciente(self):
        del self.fila[0]
    
    def chamaProximo(self):
        proximo = self.fila[0]
        self.removePaciente()
        return proximo

    def visualizarFila(self):
        if len(self.fila) > 0:
            for paciente in self.fila:
                print(paciente)
            return
        print('Não há pacientes na fila.')
    
    def tamanhoDaFila(self):
        return len(self.fila)
    


    