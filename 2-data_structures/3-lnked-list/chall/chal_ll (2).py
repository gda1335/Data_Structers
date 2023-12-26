
# node class
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
    
    def push(self,new_data):
        #linked list basina node ekle
        #node yarat ve icindeki veriyi belirle
    

        new_node = Node(new_data)
        
        # yeni node kendisinden sonra gelen node'u isaret etsin
        new_node.next = self.head
        
        # head yeni node'u isarate etsin
        self.head = new_node
    
    def insertAfter(self,prev_node,new_data):  #onceki koddan farkli olan -1 ortaya eklemek
        """
        verilen(prev_node) node'dan sonra yeni node ekle
        """
        
        # prev_node var mi yok mu onu kontrol et
        if prev_node is None:
            print("boyle bir node yok")
            return
        # yeni node yarat ve icerisine veri koy
        new_node = Node(new_data) 
        
        # new_node next'ini prev_node next'i yap
        new_node.next = prev_node.next
        
        # prev_node next'i new node yap
        prev_node.next = new_node
        
    def append(self,new_data):  #onceki koddan farkli olan -2 sondan eleman eklemek
        """
        linked list sonuna node eklemek
        """
        # 2-1-yeni node yarat daha sonra icerisine new_data verisini depola
        new_node = Node(new_data)
        
        # 2-2-eger linked list bos ise yeni eklenen node head olsun
        if self.head is None:
            self.head = new_node 
            return
        
        #3-#eger bos degilse --- linked list'in head'inden basla sonuna kadar git SONA NODE EKLİCEZ
        last = self.head   
        while last.next: #none mi bir sonraki none ise yap 
            last = last.next
        
        # 4- last.next None. onun yerine new_node ekle
        last.next = new_node
        
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
linked_list.push("tail")
linked_list.push(15)
linked_list.push(25)
linked_list.push("head")
linked_list.printLinkedList()

linked_list.insertAfter(linked_list.head,100)
linked_list.printLinkedList()

linked_list.append("son")
linked_list.printLinkedList()