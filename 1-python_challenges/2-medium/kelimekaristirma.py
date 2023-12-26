#kelime karistirma

#ankara--> kaarna ---> True False turns


def HarfKar(str1,str2):
    #str2 ' deki harfe erisim'
    #check str1 obur str.
    #true or false?
    
    for i in str2:
        if i not in str1:
            return False
        
        return True
        
#print(HarfKar("ankara","karana"))



print(HarfKar("makarna", "ankara"))

    
    
 #%%
def kelimeKaristirmak(str1,str2):
    a=[]
    b=[]
    if len(str1) == len(str2):
        for i,j in zip(str1,str2):
            a.append(i in str2)
            b.append(j in str1)
        print(all(a)&all(b))    
    else:
        print("false")
kelimeKaristirmak("izmir", "aaimir")
