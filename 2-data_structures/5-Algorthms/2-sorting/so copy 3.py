def selection_sort(arr):
    """
    selection sort
    """
    for i in range(len(arr)-1,0,-1):  #geriye dogru -->en sondaki nden basla siralamaya
        positionOfmax = 0
        
        for location in range(1, i + 1):
            if arr[location] > arr[positionOfmax]:
                positionOfmax = location  #yer degistirme yaptik
        print(positionOfmax)
        temp = arr[i]
        arr[i] = arr[positionOfmax]  
        arr[positionOfmax] = temp
        print(arr)
    return arr

arr=[1333,24,67,54645,43,34,68,4]



selection_sort(arr)
#en kucuk olani bul gez ve bulunca ind 0 'a at

#varsa yer degistir daha kucuk bulursan aradıgın hangisiyse mesela en sonda buldun elemanila onu yer degistir
