class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
    def __str__(self):
        return f"<- {self.data} -> "
        
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev

    def setNext(self,next):
        self.next = next
    
    def setPrev(self,prev):
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
        else:
            aux = self.head
            while aux.getNext():
                aux = aux.getNext()
            aux.setNext(newNode)
            newNode.setPrev(aux)
        self.tail = newNode
        
    def preApend(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.setPrev(newNode)
            newNode.setNext(self.head)
            self.head = newNode
    
    def appendAfter(self,data,ref):
        newNode = Node(data)
        if self.tail.data == ref:
            self.tail.setNext(newNode)
            newNode.setPrev(self.tail)
            self.tail = newNode
        else:
            aux = self.head
            while aux.data != ref:
                aux = aux.getNext()
            newNode.setPrev(aux)
            newNode.setNext(aux.getNext())
            aux.getNext().setPrev(newNode)
            aux.setNext(newNode)
    
    def appendBefore(self,data,ref):
        aux = self.head
        while aux:
            if aux.prev == None and aux.data == ref:
                self.preApend(data)
            elif aux.data == ref:
                newNode = Node(data)
                aux.getPrev().setNext(newNode)
                newNode.setNext(aux)
                aux.setPrev(newNode)
                newNode.setPrev(aux.getPrev())
            aux = aux.getNext()


    
    def printList(self):
        aux = self.head
        while aux:
            print(aux,end="")
            aux = aux.getNext()


dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.preApend(0)
dll.appendBefore(2.5,3)
dll.appendAfter(10,4)
dll.appendBefore(9,10)
dll.printList()
