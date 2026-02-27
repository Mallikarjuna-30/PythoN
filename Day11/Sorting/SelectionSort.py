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

# Example: [29,10,14,37,13]

# i = 0 (min = 0)
# Find smallest in [29,10,14,37,13]. It's 10 at index 1.
# Swap 29 and 10.
# Array: [10, 29, 14, 37, 13]

# i = 1 (min = 1)
# Find smallest in [29,14,37,13]. It's 13 at index 4.
# Swap 29 and 13.
# Array: [10, 13, 14, 37, 29]

# i = 2 (min = 2)
# Find smallest in [14,37,29]. It's 14 at index 2.
# Swap 14 and 14 (no change).
# Array: [10, 13, 14, 37, 29]

# i = 3 (min = 3)
# Find smallest in [37,29]. It's 29 at index 4.
# Swap 37 and 29.
# Array: [10, 13, 14, 29, 37]

# i = 4 (min = 4)
# Find smallest in [37]. It's 37 at index 4.
# Swap 37 and 37 (no change).
# Array: [10, 13, 14, 29, 37]

# i = 5 (min = 5)
# Find smallest in [37]. It's 37 at index 4.
# Swap 37 and 37 (no change).
# Array: [10, 13, 14, 29, 37]

# Array is sorted.