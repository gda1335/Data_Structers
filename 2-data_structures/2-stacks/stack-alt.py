class Stack:
    def __init__(self):
        self.items = []
 
    def push_(self, data):
        self.items.insert(0, data)
 
    def pop_(self):
        return self.items.pop(0)
 
    def __repr__(self):
        return f'{self.items}'
 
stck = Stack()
stck.push_(40)
stck.push_(50)
stck.push_(60)
stck.push_(70)
stck.push_(80)
stck.push_(90)
 
print(stck)
print(stck.pop_())
print('******')
print(stck)