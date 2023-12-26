import itertools

def ThreeSum(arr):
    # Hedef sayıyı al
    n = arr[0]
    # İlk elemanı listeden kaldır
    del arr[0]
    
    # Kombinasyonlar için tüm indisleri içeren bir liste oluştur
    l = range(len(arr))
    # Tüm 3 elemanlı kombinasyonları al
    comb = itertools.combinations(l, 3)
    
    for i in comb:
        s = 0
        for j in i:
            # Kombinasyondaki indisleri kullanarak elemanları topla
            s += arr[j]
        
        # Toplam, hedef sayıya eşit mi kontrol et
        if s == n:
            return "True"
    
    # Hiçbir kombinasyon hedef sayıya ulaşamadı
    return "False"
