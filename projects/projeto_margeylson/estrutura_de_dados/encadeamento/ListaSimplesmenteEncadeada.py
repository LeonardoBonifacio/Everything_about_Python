from elemento import Elemento

class ListaEncadeada:
    def inicializaLista(self,primeiroValor):
        self.head = Elemento(primeiroValor)
        self.tail = self.head
    
    def insereElementoNoInicio(self, valor):
        novo = Elemento(valor)
        novo.ligaCom(self.head)
        self.head = novo
    
    def insereElementoNoFim(self, valor):
        novo = Elemento(valor)
        if self.head == None:
            self.head = novo
            return
        atual = self.head
        while atual.ligacao != None:
            atual = atual.ligacao
        atual.ligacao = novo
    
    def removePrimeiraAparição(self,valorProcurado):
        atual = self.head
        anterior = None
        while atual != None and atual.valor != valorProcurado:
            anterior = atual
            atual = atual.ligacao
        if atual == None:
            print("Valor não encontrado -> " + str(valorProcurado))
            return
        anterior.ligacao = atual.ligacao
    
    def procuraValorNaLista(self,valorProcurado):
        if self.head == None:
            return False
        atual = self.head
        while atual != None:
            if atual.valor == valorProcurado:
                return True
            atual = atual.ligacao
        return false
    
    def exibirElementos(self):
        atual = self.head
        while atual != None:
            print(atual.valor,end=" -> ")
            atual = atual.ligacao
        print('Fim')

lista = ListaEncadeada()
lista.inicializaLista(10)
lista.insereElementoNoFim(11)
lista.insereElementoNoInicio(9)
lista.removePrimeiraAparição(14)
if lista.procuraValorNaLista(10):
    print("10 está na lista")
else:
    print("10 não esta na lista")
lista.exibirElementos()