
def word(liste):

    a=liste[0]

    b=liste[1].split(",")

   

    for i in range(len(a)):

        k=a[:i+1]

        l=a[i+1:]
        #cok acik

        if k in b and l in b :

            return k +" ,"+l

    return "bulunmadi"