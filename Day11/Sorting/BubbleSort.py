#<----- Bubble Sort ---->#

def bubbleSort(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr)-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

print(bubbleSort([1,4,3,6,2,5]))




















#<----- How it works ----->#

# 1. Start from the first element (index 0).
# 2. Compare it with the next element.
# 3. If the current element is greater than the next element, swap them.
# 4. Repeat until the array is sorted.

# Example: [15,16,6,8,5]

# i = 0
# Compare 15 and 16. 15 < 16, no swap.
# Array: [15, 16, 6, 8, 5]
# Compare 16 and 6. 16 > 6, so swap.
# Array: [15, 6, 16, 8, 5]
# Compare 16 and 8. 16 > 8, so swap.
# Array: [15, 6, 8, 16, 5]
# Compare 16 and 5. 16 > 5, so swap.
# Array: [15, 6, 8, 5, 16]

# i = 1
# Compare 15 and 6. 15 > 6, so swap.
# Array: [6, 15, 8, 5, 16]
# Compare 15 and 8. 15 > 8, so swap.
# Array: [6, 8, 15, 5, 16]
# Compare 15 and 5. 15 > 5, so swap.
# Array: [6, 8, 5, 15, 16]
# Compare 15 and 16. 15 < 16, no swap.
# Array: [6, 8, 5, 15, 16]

# i = 2
# Compare 6 and 8. 6 < 8, no swap.
# Array: [6, 8, 5, 15, 16]
# Compare 8 and 5. 8 > 5, so swap.
# Array: [6, 5, 8, 15, 16]
# Compare 8 and 15. 8 < 15, no swap.
# Array: [6, 5, 8, 15, 16]
# Compare 15 and 16. 15 < 16, no swap.
# Array: [6, 5, 8, 15, 16]

# i = 3
# Compare 6 and 5. 6 > 5, so swap.
# Array: [5, 6, 8, 15, 16]
# Compare 6 and 8. 6 < 8, no swap.
# Array: [5, 6, 8, 15, 16]
# Compare 8 and 15. 8 < 15, no swap.
# Array: [5, 6, 8, 15, 16]
# Compare 15 and 16. 15 < 16, no swap.
# Array: [5, 6, 8, 15, 16]

# i = 4
# Compare 5 and 6. 5 < 6, no swap.
# Array: [5, 6, 8, 15, 16]
# Compare 6 and 8. 6 < 8, no swap.
# Array: [5, 6, 8, 15, 16]
# Compare 8 and 15. 8 < 15, no swap.
# Array: [5, 6, 8, 15, 16]
# Compare 15 and 16. 15 < 16, no swap.
# Array: [5, 6, 8, 15, 16]

# Array is sorted.
