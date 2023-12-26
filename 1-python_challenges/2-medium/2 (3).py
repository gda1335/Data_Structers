#kayip basamak

"""

"10-x=4"
x ' i bul tarzi 
1x*11=121---> x kayip basamak
x=1 
x'i bul'
"""

def kayip(string):
    #x bul ---> replace et 0-9 arasi
    #bul = 
    #='den next and back compare by eval
    #return
    
    for i in range(10): #0-9 arasi deneme x icin
        c=string.replace("x",str(i)) #degistir
        x=string.index("=") # = sonraki eval ile mat islemi yaptiriyor
        if eval(c[:x]) ==eval(c[x+1]): #mat islemi yapiyor
            return str(i)
        
# print(kayip("10-x=4"))
print(kayip("1x0 /3=50"))


        
        
        