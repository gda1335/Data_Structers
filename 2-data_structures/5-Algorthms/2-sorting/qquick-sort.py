#quick sort --> pivot buyuk kısım kucuk kısım
# recursive
def quick_sort(arr):
    quick_sort_recursion(arr,0,len(arr)-1)
    return arr

def quick_sort_recursion(arr,first,last):
    
    if first < last:
        
        splitpoint = partition(arr,first,last)
        
        # left right
        quick_sort_recursion(arr,first,splitpoint - 1)
        quick_sort_recursion(arr,splitpoint + 1,last)
        
    # end point
    
def partition(arr,first,last):  #algortma yazilcagi kisim
    
    # pivot value = ilk eleman secelim. visu algo ile karsilasatirmak icin
    pivotvalue = arr[first]  #en bas pivot
    
    left = first + 1  #bir sonraki 
    right = last
    
    done = False
    
    while not done:
        
        while left <= right and arr[left] <= pivotvalue:
            left = left + 1
        while arr[right] >= pivotvalue and right >= left: #siralama
            right = right - 1
            
        if right < left:
            done = True
        else: 
            temp = arr[left] #lefti yer degistir  egere l>r ise 
            arr[left] = arr[right] #leftin  
            arr[right] = temp
        
    temp = arr[first] 
    arr[first] = arr[right]
    arr[right] = temp
    
    return right


# Bir pivot eleman seçilir (bu kodda ilk eleman seçilmiştir).
# Sol ve sağ işaretçiler (left ve right) pivot elemanın solunda ve sağındaki elemanları karşılaştırmak için kullanılır.
# Sol işaretçi, pivot elemandan büyük veya eşit olan bir elemanı bulana kadar ilerler.
# Sağ işaretçi, pivot elemandan küçük veya eşit olan bir elemanı bulana kadar geriye doğru ilerler.
# Sol işaretçinin konumu sağ işaretçinin konumundan büyükse, işlem tamamlanır ve pivot eleman ile işaretçilerin konumu değiştirilir.
# İşlem tekrarlanır ve dizinin iki alt dizisine bölünür.
# Alt diziler sıralandığında, orijinal dizi de sıralanmış olur.
# Bu şekilde devam edererek tüm alt diziler sıralanır ve sonuç olarak orijinal dizi sıralanmış olur.