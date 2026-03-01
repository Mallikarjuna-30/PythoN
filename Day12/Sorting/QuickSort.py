#<----- Quick Sort ---->#

def partition(arr,low,high):
    pivot = arr[low]
    left = low
    right = high
    
    while left < right:
        while left <= high and arr[left] <= pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    
    arr[low], arr[right] = arr[right], arr[low]
    return right
    
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr,low,pi-1)
        quickSort(arr,pi+1,high)

arr = [10,7,8,9,1,5]
quickSort(arr,0,len(arr)-1)
print(arr)


#<----- How Quick Sort Works ---->#

# 1. Quick Sort is a divide and conquer algorithm.
# 2. It picks an element as a pivot and partitions the given array around the picked pivot.
# 3. The partition() function is used for partitioning the array. The partition(arr, low, high) is a key process that assumes that arr[low..high] is sorted and partitions the array into two sub-arrays.
