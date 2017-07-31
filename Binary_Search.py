def binary_search(input_array, value):
    """Your code goes here."""
    low = 0
    high = len(input_array)-1
    while low<=high:
        mid = (high+low)/2
        if value==input_array[mid]:
            return mid
        elif value<input_array[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1
    

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
