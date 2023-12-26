
def Capital(s):
    s=s.split(" ")
    #john  wayne --> "john", "wayne"
#anymore this is list
    for i in range(len(s)): #till lenght of list , this will turn  john lennon --> john ,lennon
        s[i]=s[i][0].upper()  #capital  j+l --> "jl"
        kw="".join(s)  #only capital was added
    return kw

def no_cal(n):
    ls=""
    for  i in range(2,n+1):
        if i%2==0:  #entried numbers that is string divided into 2 and if it is even added ls 
            ls+=str(i)
    return ls[-1]+ ls[len(ls)//3]

def special_pass(name_surname,no):
    cap=Capital(name_surname)  #called first func
    nums=no_cal(no)  #called second func --> equal to any variable
    special=nums[::-1]+cap+nums
    print("parola",special)
    

#%%
cond=True
while cond:
    namesurname=input("---->")
    if type(namesurname)!=str:
    #if not namesurname.isalpha(): isalpha wants one string
        print("hatali")
        cond=False
    no=int(input("----->"))
    special_pass(namesurname, no)
    
    q=input("cikmak icin q'ya basiniz--->")
    if q=="q":
        cond=False

    
    

        


        
        




