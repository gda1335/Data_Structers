#array pairs

#i[5,6,6,5,3,3] tersten gidincde pair kendisi dısında olcak.kendisine esitse ok bas.


def coup(array):
    #liste
    d=[]
    l=len(array)
    for i in range(0,l-1): #cifter cifter aliyor
        if array[i]==array[i+1]:
            print("ok")
            d.append(array[i])
    return d
            

        #ben yapamadım :/
        
    
coup([1,2,2,23,36])
    