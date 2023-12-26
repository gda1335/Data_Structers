# #three sum

# * Input: 10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2  => 10 = (2,3,5) (3,3,4) (5,1,4)
# * Output:"true"
# * 
# * Input: 12, 3, 1, -5, -4, 7
# * Output:"false"
#bu elemanlarin toplami 10 edicek
#%%
import itertools
def ThreeSum(arr):
    n=arr[0] #elde edilcek sayi
    del arr[0]  
    print(arr)
    l=range(len(arr))
    comb=itertools.combinations(l,3)  # 3 elemanli komb
    for i in comb:
        print(i)
        s=0
        for l in i:
            s+=l
            print(s)
        if s==n:
            return "True"
    return "False"

arr=[10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2]
#ilk elm silindi

ThreeSum(arr)
