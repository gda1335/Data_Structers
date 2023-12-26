
#algoritma
def multiplication(koyun_sy,ortfyt):
    return koyun_sy*ortfyt

print(multiplication(20,5))

#%% code complexity

#kare toplami --> 1

def sq(n):
    tot=0
    for x in range(1,n+1):
        tot+=x**2
        
    return tot

print(sq(5))
#%%

#esdeger

def sq2(n):
    return (n*n+1*(2*n+1))/6

print(sq(5))

#timeit deneyince 2> 1 effective

#bu  hardware'e bagli olan bir sey cok seyi etkilemez
#%% big o ornekler

#run  time 'a gore karsiastirma!
#%%

#o n 
def pr(liste):
    print(liste[0])


print(pr([-5,1,1,23,5]))


#constant big o -- inputt boyutundan bagimsiz


#%%
# o n linear

"""

input size ile orantili !!

"""


def linear(liste):
    
    for d in liste:
        print(d)  # d liste boyutu kadar doncek
        
        
        
linear([1,24])

#icine liste aliyor
    
#input size ile orantili
#%%  3 tane ne kere cevircek


#cubic---< nested looptan olusan 3 for 


def cubic(liste):
    for i in liste:
        for j in liste:
            for k in liste:
                print(i,j,k)



cubic([1,2,3])

#27 kez islem yapti!!
# =============================================================================
# 
# 
# #onemli sorular!!
# #---------------------
# 
# 
# for x i n range (n):
#     #jjdhkjdh
#     for y in range(n):
#         print(y)
# #ans: o n^2
# 
# 
# 
# 
# 
# for x i n range (n):
#     #jjdhkjdh
# 
# #ans:o(n)
# 
# for x i n range (n):
#     #jjdhkjdh
# for x i n range (n):
#     #jjdhkjdh
# for x i n range (n):
#     #jjdhkjdh
#     
#     
# #ans: o n
# =============================================================================




    
    
    
    
    
    
    
    
    
    
    
    



