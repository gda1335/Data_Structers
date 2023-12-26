def rec_binary_search(arr,ele):
    """
    binary search with recursion
    """
    
    # base case
    if len(arr) == 0:
        return False
    
    # recursive case
    else:
        mid = int(len(arr)/2)
        
        # if match found (base)
        if arr[mid] == ele:
            return True
        else:
            # lower
            if ele < arr[mid]: #last indexim middle oldu arr'in degeri mid oldu bastan oraya kadar al!
                return rec_binary_search(arr[:mid],ele)
            
            # upper
            else:
                return rec_binary_search(arr[mid+1:],ele) #ilk indexim mid+1 den baslicak eger upper icindeyse 
            
            #bazen mid olan elemani da dahil ediyorlar


liste = [3,6,11,12,18,21,34]
rec_binary_search(liste,18)

#basit slicing

