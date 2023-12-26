#%%
def sqSorderlist(liste,val):
    """sq for order list"""
    idx=0
    found=False
    stop=False

    while idx<len(liste) and not found and not stop:
        if liste[idx]==val: #bulma durumu
            found=True
        else:
            if val<liste[idx]:  #kucuk olma durumu direk kes,yani o deger a artık coktan listeden gecmis
                stop=True
            else:
                idx+=1
    return(found,idx)

liste=[2,3,4,5,7,9]

val=5
found,idx=sqSorderlist(liste,val)

print(found)
print(idx)





