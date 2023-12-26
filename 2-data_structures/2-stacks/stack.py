class Stack: #class+ constructor   lifo ozelligi var
    
    def __init__(self):
        """
        initialize (constructor)
        """
        self.items = [] #bos eleman 
        
    def isEmpty(self):
        """
        bos olup olmadigini kontrol eder
        """
        return self.items == []  # boolean operation -- t f 
    
    def push(self,item):
        """
        stack'e item ekler
        """
        self.items.append(item) #eleman ekleme
    
    def pop(self):
        """
        stack'ten item cikarma
        """
        return self.items.pop() #pop method
    
    def top(self):
        """
        stack icerisindeki son item'i gosterir
        """
        return self.items[len(self.items)-1] 
    
    def size(self):
        """
        size of stack
        """
        return len(self.items) #boyutu
    

stack = Stack()
print(stack.isEmpty())

stack.push("ankara")  #ekleme
print(stack.top())

stack.push("istanbul") #ekleme
print(stack.top())

stack.push("izmir") #ekleme
print(stack.top())
#ekleme

print(stack.size())

stack.pop() #izmir cikti
print(stack.top()) #en tepedeki ankara

stack.pop() #ankara gitti 
print(stack.top()) #istanbul

print(stack.isEmpty()) #istanbul var

stack.pop() #onuda attik
print(stack.isEmpty())     #true dondu