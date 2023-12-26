#%%calculating big o


#in signifacnt constant


def pr(liste):
    for i in liste:
        print(i)  # for da n defa


print(pr([-5,1,1,23,5]))


# o n kadar

#%%
def o_2(liste):
    for i in liste:
        print(i)
    for j in liste:
        print(j)


print(o_2([-5,1]))
#o=2n  2 ihmal edilebilir.

#%%
#on+1

def pr(liste):
    print(liste[0])  #o1--> size 'a bagli degil
    
    for i in liste:  # o n dir 
        print(i)


print(pr([-5,1,1,23,5]))

#o n+1 ama 1 ihmal edildi.
