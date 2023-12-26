def insertion_sort(arr):
    """
    insertion sort
    """
    for i in range(1,len(arr)):
        
        currentvalue = arr[i]
        position = i
        
        # sublist
        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position -1]
            position -= 1
        arr[position] = currentvalue
    return arr

#https://visualgo.net/en/sorting?slide=1