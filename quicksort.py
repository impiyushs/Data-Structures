def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array)-1
    if high - low < 1:
        return array
    else:
        pivot=high
        j=low
        while 1:
            if j == pivot:
                break
            elif array[j]>array[pivot]:
                temp=array[pivot]
                array[pivot]=array[j]
                array[j]=array[pivot-1]
                array[pivot-1]=temp
                pivot=pivot-1
            else:
                j+=1
        quicksort (array, low, pivot-1)
        quicksort (array, pivot+1, high)
        return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)
