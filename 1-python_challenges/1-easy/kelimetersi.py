#kelime tersi
#en basic *-->
def kel(a):
    return a[::-1]
print(kel("istanbul"))


#%% bos str ile toplamak
def tersi(f):
    ters="" #bos str ile toplamak baska bir yontem!

    ters=ters+f[::-1]
    return ters
print(tersi("istanbul"))
        



#%% 2.methodla ayni
def tersim(a):
    return "".join(reversed(a)) #direk reversed alip bu stringi "" bos str 'ye join ediyor


print(tersim("istanbul"))


    