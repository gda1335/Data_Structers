#listeyi random yapip sorted yapma...

mylist=[0,1,2,3,4,5,6,7,8]
from random import shuffle #karistirdik
shuffle(mylist)
print("shuffled: ", mylist)
mylist.sort()
print("sorted: ",mylist)

#%% join ve strip methodu

yeni=".".join("friends")
print(yeni)

first=yeni.split(".") #listeye cevirdi
print(first) #harfleri , ile ayirdi...

j = "".join(first)
print(j)  #tekrar birlestiridk


#keywordler identifier olarak kullanilmaz!

# * Başında olan boşluk leading whitespace
# * Sonunda olan boşluk trailing whitespace
string = '   datai   '
print(string.lstrip()) # ondeki boslugu yok et
print(string.rstrip()) # arkadaki boslugu yok et
print(string.strip())  # ondeki ve arkadaki boslukları yok et


#lower -- tumunu kucuk harf
#upper tumu buyuk harf
#capitalize : sadece bas harf


# #-------
# / bolu 
# // bolme integer dondrr
# % kalani






