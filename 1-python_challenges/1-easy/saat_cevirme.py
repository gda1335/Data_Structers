#saat cevirme

#saat ve dk 'ye cevirme

def hesap(s):
    #saati bulmak
    #geri kalan dk 
   saat= s//60 
   dk=s%60 #modulus op (bunu bile unutmusum kendime tebrik)
   return str(saat)+ "." + str(dk)


print(hesap(130))
    