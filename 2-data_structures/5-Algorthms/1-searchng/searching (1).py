
#%%
def lsearch(liste,val):
    """sequential search"""
    idx=0
    found=False
    while idx<len(liste) and not found:
        if list[idx]==val:
            found=True
        else:
            idx+=1
        return(found,idx)
    
l1=[5,4,7,9,3]
#fonksi

found,idx=lsearch(l1,4)
print(found)
print(idx)