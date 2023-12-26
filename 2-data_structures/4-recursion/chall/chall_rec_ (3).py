#uslu 

# 2 ve 3 2.2.2 =3

def multiply(x,y):
    #base case
    if y==0:
        return 0
    return x+multiply(x,y-1)

def power(a,b):
    #base case 
    if b==0:
        return 1
    #recursion
    return multiply(a,power(a,b-1))
    

    """
    2,3
    pwer 2,3 :8
    multiply(2,power(2,2))4 
    mutiply(2,power(2,1)) 2 
    multiply(2,power(2,0)) 1
 





    """