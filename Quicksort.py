def partition(array, low, high):
    pivot = array[high]
  
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1
def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)
array = [9,1,9898,98,7,-3,5,6,4]
print("original array:",array)
size=len(array)
quicksort(array,0,size-1)
print("the sorted array:",array)