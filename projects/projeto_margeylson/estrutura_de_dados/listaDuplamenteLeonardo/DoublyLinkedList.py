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
            if aux.prev == None and aux.data == ref:# Append before the head
                self.preApend(data)
            elif aux.data == ref: # prev newnode aux 
                newNode = Node(data)
                aux.getPrev().setNext(newNode)
                newNode.setNext(aux)
                newNode.setPrev(aux.getPrev())
                aux.setPrev(newNode)
            aux = aux.getNext()
    
    def deleteNode(self,nodeWithData):
        aux = self.head
        while aux:
            if aux == self.head and aux.data == nodeWithData:
                if aux.getNext() == None:#Deleting the head of a empty list
                    aux = None
                    self.head = None
                    return
                else:
                    nxt = self.head.getNext() #Deleting the head of a not empty list
                    aux.setNext(None)
                    aux = None
                    nxt.setPrev(None)
                    self.head = nxt
                    return
            elif aux.data == nodeWithData:
                if aux.getNext():# Removing a node that's not the head either the tail
                    nxt = aux.getNext()
                    prev = aux.getPrev()
                    prev.setNext(nxt)
                    nxt.setPrev(prev)
                    aux.setNext(None)
                    aux.setPrev(None)
                    aux = None
                    return
                else: # Remmoving the tail
                    prev = aux.getPrev()
                    prev.setNext(None)
                    aux.setPrev(None)
                    aux = None
                    self.tail = prev
                    return
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
dll.append(5)
dll.append(6)
dll.appendBefore(4.5,5)
dll.printList()