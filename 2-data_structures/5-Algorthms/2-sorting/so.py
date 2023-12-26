def bubbleSort(arr):
    for r in range(len(arr)-1,0-1)  #arr size eleman sayisi azaldikca degisecek karsilastirma yaparken arr size i azalcak
     #eleman sayim azalarak gidiyor
     for  k in range(r): #elemna sayisi al
        if arr[k]>arr[k+1]:
           temp=arr[k]
           arr[k]=arr[k+1]  #yer deistirme islemi
           arr[k+1]=temp
    return arr


