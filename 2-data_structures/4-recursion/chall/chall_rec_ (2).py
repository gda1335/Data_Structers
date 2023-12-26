def multiply(x,y):
    #base case
    if y==0:
        return 0
    return x+multiply(x,y-1)

    #recursion
"""
2*3
2 2 2

2+multipl(2,0) -->2 
2+  mutlt(2,1) -->4
2+mlyp(2,2) --> 2+4 =6
"""
