# 2 stacks ile queue yapmak
class queuetostack():
    def __init__(self):
        self.stack1=[]
        self.stack2=[]

#stack e item ekleme ama que yaratmak icin
    def enqueue(self,item):
        self.stack1.append(item)
#stack1 icine pop yaparak stack2ye item yolla
    def dequeue(self):
        if not self.stack2:
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()




queue=queuetostack()
queue.enqueue("1")
queue.enqueue("2")
queue.enqueue("3")



print(queue.dequeue())


print(queue.dequeue())



#stack1
#tsack2
#que