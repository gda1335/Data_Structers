#bas harf buyutme !!  Review!!!

#my method:
def BasHa(e):
    e=e.split()
    for i in e:
        g=i.capitalize()
        print(g)
        


print(BasHa("kod yazmak cok guzel"))


#deneme
#Split stringi bir listeye cevirir.
# =============================================================================
# a="istanbul cok guzel"
# a=a.split()
# for i in a:
#     h=i.capitalize()
#     print(h)
# 
# =============================================================================


#alternatif1

def Basharf(str):
    #split ile bosluklari ayir listeye cvir
    
    kelm=str.split(" ")
    
    
    for i in range(0,len(kelm)):
        kelm[i]=kelm[i][0].upper()+ kelm[i][1:] #str topluyo
        #birlestir
    return " ".join(kelm)


print(Basharf("istanbul cok guzel"))


#method ile tek satir
#%% metod olarak!
den="los angeles new york"


b=den.title()       

print(b)


#%% 3 eylul 2023


str1="hello naber nasilsin"

lst=str1.split(" ")
arr=[]
for i in lst:
    i=i.capitalize()
    
    arr.append(i)
    

print(arr)












