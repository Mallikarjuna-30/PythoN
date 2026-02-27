#<---- Selection Sort ---->#

def Selectionsort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min] = arr[min],arr[i]
    return arr

print(Selectionsort([1,3,2,8,4,5]))


#<----- How it works ----->#

# 1. Start from the first element (index 0).
# 2. Find the smallest element in the unsorted part of the array.
# 3. Swap it with the first element.
# 4. Move to the next element and repeat until the array is sorted.

# Example: [8,3,5,2,9,1]

# i = 0 (min = 0)
# Find smallest in [8,3,5,2,9,1]. It's 1 at index 5.
# Swap 8 and 1.
# Array: [1, 3, 5, 2, 9, 8]

# i = 1 (min = 1)
# Find smallest in [3,5,2,9,8]. It's 2 at index 3.
# Swap 3 and 2.
# Array: [1, 2, 5, 3, 9, 8]

# i = 2 (min = 2)
# Find smallest in [5,3,9,8]. It's 3 at index 3.
# Swap 5 and 3.
# Array: [1, 2, 3, 5, 9, 8]

# i = 3 (min = 3)
# Find smallest in [5,9,8]. It's 5 at index 3.
# Swap 5 and 5 (no change).
# Array: [1, 2, 3, 5, 9, 8]

# i = 4 (min = 4)
# Find smallest in [9,8]. It's 8 at index 5.
# Swap 9 and 8.
# Array: [1, 2, 3, 5, 8, 9]

# i = 5 (min = 5)
# Find smallest in [9]. It's 9 at index 5.
# Swap 9 and 9 (no change).
# Array: [1, 2, 3, 5, 8, 9]

# Array is sorted.