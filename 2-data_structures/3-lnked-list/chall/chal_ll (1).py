#list basından node eklemek

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #list  basi None -----#node yarat

class linkedList:
    def __init__(self):
        self.head=None  #baslangic adresi yok
    def push(self,new): #linked list basina node ekle
        #node yarat ve icindeki veriyi belirle
        new_node=Node(new)
        #yeni node kendisinden sonra gelen  nodu isaret etsin
        new_node.next=self.head #head bir sonraki node adr tutuyor

        #head yeni nodu isaret etsin
        self.head=new_node
    def prtlinkedlist(self):
        """linked list print eder"""
        temp=self.head
        print("linked list:")
        while temp:
            print(temp.data)
            temp=temp.next  #bir sonraki node'a gecti ve goster 
l1=linkedList()
l1.push(14)
l1.push(24)
l1.push("ilk eleman")
print(l1.prtlinkedlist())  #bitince None
#listte basina ekliyoruz  ilk eleman-- 24-14
