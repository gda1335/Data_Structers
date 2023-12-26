class Queue:
    
    def __init__(self):
        """
        initialize (constructor)
        """
        self.items = [] #bos bir veri yapisi
        
    def isEmpty(self):
        """
        bos olup olmadigini kontrol et
        """
        return self.items == [] # bool operation
    
    def enqueue(self,item):
        """
        queue item ekler
        """
        self.items.insert(0,item) #ekleme
        
    def dequeue(self):
        """
        queue dan item cikartir
        """
        return self.items.pop() #cikar
    
    def size(self):
        """
        length of items(queue)
        """
        return len(self.items)
    
que=Queue()
print(que.isEmpty())

que.enqueue("ankara")
que.enqueue("los angeles")
print("size:",que.size())

#simdi cikaralim.... sadece 1 tane


que.dequeue()
print("size:",que.size())


#%% deque
class Deque:
    
    def __init__(self):
        """
        initialize (constructor)
        """
        self.items = []
        
    def isEmpty(self):
        """
        bos olup olmadigini kontrol et
        """
        return self.items == [] # bool operation
    
    def addFront(self, item):
        """
        deque ya front kismindan item ekler
        """
        self.items.append(item) #stack gibi
        
        
    def addRear(self, item): # que eklemesi
        """
        deque ya rear kismindan yeni item ekler
        """
        self.items.insert(0,item) #basına ekleme que gibi
        
    def removeFront(self): 
        """
        deque front kismindan item cikartir
        """
        return self.items.pop()
    
    def removeRear(self):
        """
        deque rear kismindan iterm cikart
        """
        return self.items.pop(0) # en alttan 
    
    def size(self):
        """
        length of deque
        """
        return len(self.items)

dq=Deque()
print(dq.isEmpty())
dq.addFront("deep")
dq.addRear("learning")

print(dq.size())


dq.removeFront()
dq.removeRear()

print(dq.isEmpty())

