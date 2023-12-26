#array rotasyonu---> BUNU TEKRARLA!!!

#a=[2,3,4,5]
#out: 4523
#ilk eleman index kabul et ve indexe git ordan dvm ve don

# def arrayRotation(str1):
#     list_str1 = str1.split(",")
#     list_first_element = list_str1[0]
#     list_first_element = int(list_first_element)
#     list_first_part = list_str1[:list_first_element]
#     list_last_part = list_str1[list_first_element:]
#     new_list = list_last_part + list_first_part
#     new_list = "".join(new_list)
#     return new_list
 
# str1 = input("list:")
# print(arrayRotation(str1)) 


#%%

#array baslangic bul
#output array bul
#while ve counter counter++
#return


def rotateArray(x):
      return  x[x[0]:] + x[:x[0]]
        
        
print(rotateArray([2,3,5,6,6,4]))


#%%

def liste(mylist):
    mylist = list(mylist)
    result = mylist[mylist[0]:] + mylist[:mylist[0]]
    return result
print(liste((2,3,4,5)))
print(liste((4,5,6,7,8,9,10,11,12,13)))


#%%
def myFunc(arr):
    firstElem = arr[0]
    length = len(arr)
    rightSide = arr[firstElem:length]
    leftSide = arr[:firstElem]
    rightSide.extend(leftSide)
    result = "".join(map(str, rightSide))
    print(result)
print(myFunc([1,3,5,7]))



#%%

def ls(x):
    return  x[x[0]:] + x[:x[0]]

print(ls([1,2,3,4]))
