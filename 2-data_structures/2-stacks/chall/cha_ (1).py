#ters bulma


# input=[ali]---> [ila]
#creatinf stack
#definestack
def create_stack():
    stack=[]
    return stack

#stacksize

def size(stack):
    pass
def top(stack):
    pass
def isempty(stack):
    pass
def push(stack,item):
    stack.append(item)
#pop method
def pop(stack):
    return stack.pop() #remove en son 


#find reverse using stack


def reverse(string):
    n=len(string)
    stack=create_stack()
    for i in range (n):  #her harfi al 
        push(stack,string[i])  #stack ici her harf aliniyor!  #stringin  m a c h i n e ilk harften baslayip al
    new=""
    for i in range(n):
        new+=pop(stack)  #e n  cukarip new'e yazior
    return new



print(reverse("data"))


