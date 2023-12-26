#doubly ll: cift yonlu ll 

class doubly_llNode(object):
    def __init__(self,value):
        """node yarat next pointer ve prev pointeri var
        """
        self.value = value
        self.nextNode=None
        self.prevNode=None
    def setNextNode(self,node):
        self.nextNode=node
    def setPrevNode(self,node):
        self.prevNode=node
    def getNextNode(self):
        return self.nextNode
    def getPrevNode(self):
        return self.prevNode
    def getNodeValue(self):
        return self.value
    """node icerisi veri"""

izm=doubly_llNode("35")
ank=doubly_llNode("06")
ist=doubly_llNode("34")

#izm :ank:ist
#ank -- > iz
ank.setNextNode(izm)  
izm.setPrevNode(ank)
#izmir in previ de ank 
print(ank.getNextNode().getNodeValue()) #35
print(izm.getPrevNode().getNodeValue()) #06

izm.setNextNode(ist) #izmirin nexti ist
# #izm --> ist ama ist prev degil izmir'e
# print(ist.getPrevNode().getNodeValue())--- > None
#--------------baglayalim
ist.setPrevNode(izm) 

print(ist.getPrevNode().getNodeValue())
print(ist.getPrevNode().getPrevNode().getNodeValue()) #06