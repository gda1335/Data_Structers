def counting_sort(array,maxval):
    """
    count sort
    """
    n = len(array)
    m = maxval + 1
    count = [0] * m #  [0,0,0,0,0,0...,0]
    
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array