def factorial(n):
    if n==0 or n==1:
        return 1
    #base case
    else:
        return n*factorial(n-1)
factorial(4)