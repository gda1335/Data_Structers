#summation

def summation(n):
    print(n)
    if n==0:
        return 0
    else:return n+summation(n-1)

print(summation(3))

""" 3+sum2  :2 +sum1 : 1+sum0"""