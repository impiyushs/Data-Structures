def merge(array, l, m, r):
    p,q =m-l+1, r-m
    L,R = [0]*p, [0]*q
    for i in range (p):
        L[i]= array[l+i]
    for j in range (q):
        R[j]= array[m+1+j]
    i,j,k=0,0,l
    while i<p and j<q:
        if L[i]<=R[j]:
            array[k]=L[i]
            i = i+1
        else:
            array[k]=R[j]
            j = j+1
        k=k+1
    while i<p:
        array[k]=L[i]
        i,k = i+1, k+1
    while j<q:
        array[k]=R[j]
        j,k = j+1, k+1
        
def mergesort(array, l=0, r=None):
    if r is None:
        r=len(array)-1
    if r>l:
        m = (l+r)/2
        mergesort(array, l ,m)
        mergesort(array, m+1, r)
        merge(array, l, m ,r)
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print mergesort(test)
