class deque():
    def __init__(self):
        """initial
        """
        self.items=[]

    def isempty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.append(item)

    def Addback(self,item):
        self.items.insert(0,item)
        
    def removeFront(self):
        return self.items.pop()
    def RemoveBack(self):
        return self.items.pop(index=0)
    def size(self):
        return len(self.items)

dq=deque()
dq.addFront("deep")
dq.Addback("learning")
dq.size()


