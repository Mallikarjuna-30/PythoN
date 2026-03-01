#<----- Merge Sort ---->#

def mergeSort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    result = []
    i = j = 0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


print(mergeSort([12,11,13,5,6,7]))


#<----- How Merge Sort Works ---->#

# 1. Merge Sort is a divide and conquer algorithm.
# 2. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
# 3. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

