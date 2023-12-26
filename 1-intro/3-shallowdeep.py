#python 

#deep copy

import copy
old_list = [[1, 1, 1], [2, 2, 2]]
new_list = copy.deepcopy(old_list)
old_list[1][0] = 100
print("Old list:", old_list)
print("New list:", new_list)


#Burada new list degismedi deep copy metodunda

#%% shallow copy
old_list2 = [[1, 1, 1], [2, 2, 2]]
new_list2 = copy.copy(old_list2)

old_list2[1][1] = 100

print("Old list:", old_list2)
print("New list:", new_list2)
#Shallow copy: orijinal objeyi başka yeni bir objeye kopyalar
#ama orijinal obje degiştirilirse yeni obje de degisir.


#colab