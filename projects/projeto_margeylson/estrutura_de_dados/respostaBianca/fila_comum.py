class FilaComum:

    def __init__(self):
        self.fila_comum = []

    def is_empty(self):
        check = False
        if len(self.fila_comum) == 0:
            check = True
        return check
    
    def enqueue(self, paciente):
        self.fila_comum.append(paciente)

    def dequeue(self):
        if not self.is_empty():
            print(f"Chamando {self.fila_comum[0]}")
            del self.fila_comum[0]

    def visualizar_fila(self):
        if not self.is_empty():
            for paciente in self.fila_comum:
                print(paciente)
