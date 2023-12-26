#heap sort
def secondGreatlow(arr):
    
    unique = set(arr)
    print(unique)
    
    sortedlist = sorted(unique)
    print(sortedlist)
    
    if len(sortedlist) < 2:
        return str(sortedlist[0] +  " "+sortedlist[0])
    else:
        return str(sortedlist[1]) +  " "+ str(sortedlist[len(sortedlist)-2])
