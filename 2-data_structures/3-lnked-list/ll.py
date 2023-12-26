#singly linked list

class Node(object):
    #node yarat ve veriyide al ve next pointeri tut
    def __init__(self,value):
        self.value=value
        self.next = None  #bagli degil
                                            
    def setNextNode(self,node):
        self.nextnode=node
    def getNextNode(self):
        return self.nextnode
    def getNodeValue(self):
        return self.value
    
# # node sehir node value sehir plakasi 

ank=Node("06")
bolu=Node("14")
ist=Node("34")  #bos nodeler yapildi

# ank--> bolu 

ank.setNextNode(bolu)
print(ank.getNextNode()) #pointer adr
print(ank.getNextNode().getNodeValue()) #pointer adr ve icindeki deger 

bolu.setNextNode(ist)
print(bolu.getNextNode().getNodeValue()) #pointer adr ve icindeki deger 

#ank -- bolu -- ist

print(ank.getNextNode().getNextNode().getNodeValue()) #pointer adr ve icindeki deger 

#ank :: ist  :34


