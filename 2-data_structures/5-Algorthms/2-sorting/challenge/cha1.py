#second great  second low

"1 2 3 4 90 "
# 2   4 

#1 42 42 180 ----> 42 42 

def seconGandLow(arr):
    unique=set(arr)
    print(unique)
    sortedL=sorted(unique) #timsort kullanir
    print(sortedL)
    if len(sortedL)<2:
        return sortedL[0]+" "+sortedL[0]  #direk o iki elemani yoksa tek elemani 2 kere dondurur---1
    else:
        return str(sortedL[1])+ " "+str(sortedL[len(sortedL)-2])  #straightvforward--2
    
ar=[1,2,3,3,4,57,298] # 2ve 57 
print(seconGandLow(ar))