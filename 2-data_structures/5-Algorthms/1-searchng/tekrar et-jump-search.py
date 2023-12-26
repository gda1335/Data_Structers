#%%
import math

def jumpSearch(arr, x):
    n = len(arr)
    step = int(math.sqrt(n))  # Adım büyüklüğü hesaplanır
    
    prev = 0
    
    # Adımları atlayarak ileri gitmek için bir döngü
    while arr[min(step, n)-1] < x: #degerimden kucuk old surece step arttır jump
        prev += 1
        prev = step
        step += int(math.sqrt(n)) #step i step size kadar arttır
        
        if prev >= n:
            return -1 #hatali
    
    # Küçük bir aralık içinde lineer arama yapma
    while arr[prev] < x:  #onceki < degerims
        
        if prev == min(step, n):
            return -1
    
    if arr[prev] == x:
        return prev  #linear search
    
    return -1

# Test verisi
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 5

# Jump Search işlevini çağırma
result = jumpSearch(arr, x)

if result != -1:
    print(f"{x} öğesi dizinin {result}. indeksinde bulundu.")
else:
    print(f"{x} öğesi dizide bulunamadı.")

