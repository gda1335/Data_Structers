#binary search 
#%%
def binarySearch(liste,value):
    """
    binary search for sorted array (sirali liste)
    """
    first_index = 0
    last_index = len(liste) - 1
    
    found = False
    
    while first_index <= last_index and not found:
        
        middle_index = int((first_index + last_index)/2)
        
        if liste[middle_index] == value:
            found = True
        else: 
            # lower half
            if value < liste[middle_index]:
                last_index = middle_index - 1
                print("lower half")
            # upper half
            else:
                first_index = middle_index + 1
                print("upper half")
    return found
liste=[1,2,23,34,46,57,90,111,112,223,444,778,790,800]
binarySearch(liste,34)
