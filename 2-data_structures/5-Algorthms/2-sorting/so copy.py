#merge sort: recursive ddir
def merge_sort(arr):
    """
    merge sort
    """
    if len(arr) > 1:
        mid = int(len(arr)/2)
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        
        merge_sort(lefthalf)
        merge_sort(righthalf)
        
        i = 0 #sol
        j = 0 #sag 
        k = 0 #genel liste
        #siralama
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                arr[k] = lefthalf[i]  #kuucuk olN BU
                i += 1
            else:
                arr[k] = righthalf[j]
                j += 1
            k += 1
                    
        while i < len(lefthalf):
            arr[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            arr[k] = righthalf[j]
            j += 1
            k += 1
            
    return arr