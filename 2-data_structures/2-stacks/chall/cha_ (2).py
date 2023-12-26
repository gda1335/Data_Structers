#listeyi stack gibi kullnm

stack=["machine","ai","dl"]
stack.append("deep")  #stack in en ustunde

stack.append("learning")
print(stack)

print(stack.pop())

print(stack)

print(stack.pop())
print(stack)  #bastaki haline

#%% liste ve deque kullanarak queue yapmak

from collections import deque
queue=deque(["machine","ai","dl"])  #saga dogru giden bir sıra dusun
print(queue)
queue.insert(0,"deep")
print(queue)
queue.pop()
print(queue)



