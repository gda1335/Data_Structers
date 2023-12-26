#node silmek

#ank bolu ist: boluyu depolayan node'u sil
#key = bolu linked list ici bolu olan nodeu bul ve sil
#sonuc : ank ist

class Node(object):
    
    def __init__(self,data):
        """
        node initialize node yarat
        """
        self.data = data
        self.next = None  #list  basi None -----node yarat

# linked list class
class LinkedList(object):
    
    def __init__(self):
        """
        head initializer
        """
        self.head = None #baslangic adresi yok
    
    def push(self,new_data): #yeni ekleyen nodeu head yaoar
        #linked list basina node ekle
        #node yarat ve icindeki veriyi belirle
        new_node = Node(new_data)
        
        # yeni node kendisinden sonra gelen node'u isaret etsin
        new_node.next = self.head
        
        # head yeni node'u isarate etsin
        self.head = new_node

    def deleteNode(self,key):
        #istenilen key'e gore sil
        temp=self.head

        #node istenişlen degere sahipse
        if temp is not None:
            if temp.data==key:
                self.head=temp.next
                temp=None
                return temp


        # keyi ara silmek icin
        while temp is not None:
            if temp.data==key:
                break
            prev=temp
            temp=temp.next


        #nodu sil
        prev.next=temp.next


        
    def printLinkedList(self):
        """
        linked list print eder
        """
        temp = self.head
        print("Linked list: ")
        while temp:
            print(temp.data)
            temp = temp.next
linked_list = LinkedList()
linked_list.push("istanbul")
linked_list.push("bolu")
linked_list.push("ankara")
linked_list.printLinkedList()

linked_list.deleteNode("bolu")
linked_list.printLinkedList()
