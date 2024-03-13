class FilaEmergencia:

    def __init__(self):
        self.fila_emergencia = []

    def is_empty(self):
        check = False
        if len(self.fila_emergencia) == 0:
            check = True
        return check
    
    def enqueue(self, paciente):
        self.fila_emergencia.append(paciente)

    def dequeue(self):
        if not self.is_empty():
            print(f"Chamando {self.fila_emergencia[0]}")
            del self.fila_emergencia[0]

    def visualizar_fila(self):
        if not self.is_empty():
            for paciente in self.fila_emergencia:
                print(paciente)
                