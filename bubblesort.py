def bubblesort(array):
    for i in range (0,len(array)-1):
        for j in range(0,len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1], array[j]
    return array

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print bubblesort(test)
