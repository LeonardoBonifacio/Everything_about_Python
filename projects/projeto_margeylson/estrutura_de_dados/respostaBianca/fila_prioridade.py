class FilaPrioridade:

    def __init__(self):
        self.fila_prioridade = []

    def is_empty(self):
        check = False
        if len(self.fila_prioridade) == 0:
            check = True
        return check
    
    def enqueue(self, paciente):
        self.fila_prioridade.append(paciente)

    def dequeue(self):
        if not self.is_empty():
            print(f"Chamando {self.fila_prioridade[0]}")
            del self.fila_prioridade[0]

    def visualizar_fila(self):
        if not self.is_empty():
            for paciente in self.fila_prioridade:
                print(paciente)
                