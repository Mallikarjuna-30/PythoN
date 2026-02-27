#<----- Insertion Sorting ----->#

n = int(input("Enter the number of eleents : "))
arr = []
for i in range(n):
    arr.append(int(input()))

print(arr)
def insertionSort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and temp<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
    return arr

print(insertionSort(arr))



#<----- How it works ----->#

# 1. Start from the second element (index 1).
# 2. Compare it with the element before it.
# 3. If the previous element is larger, swap them.
# 4. Continue moving left and swapping until the element is in its correct sorted position.

# Example: [8,3,5,2,9,1]

# i = 1 (temp = 3)
# Compare 3 with 8. 8 > 3, so shift 8 to the right.
# Array becomes: [8, 8, 5, 2, 9, 1]
# Insert 3 at the beginning.
# Array: [ 3, 8, 5, 2, 9, 1]

# i = 2 (temp = 5)
# Compare 5 with 8. 8 > 5, so shift 8 to the right.
# Array becomes: [3, 8, 8, 2, 9, 1]
# Insert 5.
# Array: [3, 5, 8, 2, 9, 1]

# i = 3 (temp = 2)
# Compare 2 with 8. 8 > 2, shift 8.
# Array: [3, 5, 8, 8, 9, 1]
# Compare 2 with 5. 5 > 2, shift 5.
# Array: [3, 5, 5, 8, 9, 1]
# Compare 2 with 3. 3 > 2, shift 3.
# Array: [3, 3, 5, 8, 9, 1]
# Insert 2.
# Array: [2, 3, 5, 8, 9, 1]

# i = 4 (temp = 9)
# Compare 9 with 8. 8 < 9, so 9 is already in the correct position.
# Array: [2, 3, 5, 8, 9, 1]

# i = 5 (temp = 1)
# Compare 1 with 9. 9 > 1, shift 9.
# Array: [2, 3, 5, 8, 9, 9]
# Compare 1 with 8. 8 > 1, shift 8.
# Array: [2, 3, 5, 8, 8, 9]
# Compare 1 with 5. 5 > 1, shift 5.
# Array: [2, 3, 5, 5, 8, 9]
# Compare 1 with 3. 3 > 1, shift 3.
# Array: [2, 3, 3, 5, 8, 9]
# Compare 1 with 2. 2 > 1, shift 2.
# Array: [2, 2, 3, 5, 8, 9]
# Insert 1.
# Array: [1, 2, 3, 5, 8, 9]

# i = 4 (temp = 1)
# Compare 1 with 6. 6 > 1, shift 6.
# Array: [2, 4, 5, 6, 6, 3]
# Compare 1 with 5. 5 > 1, shift 5.
# Array: [2, 4, 5, 5, 6, 3]
# Compare 1 with 4. 4 > 1, shift 4.
# Array: [2, 4, 4, 5, 6, 3]
# Compare 1 with 2. 2 > 1, shift 2.
# Array: [2, 2, 4, 5, 6, 3]
# Insert 1 at the beginning.
# Array: [1, 2, 4, 5, 6, 3]

# i = 5 (temp = 3)
# Compare 3 with 6. 6 > 3, shift 6.
# Array: [1, 2, 4, 5, 6, 6]
# Compare 3 with 5. 5 > 3, shift 5.
# Array: [1, 2, 4, 5, 5, 6]
# Compare 3 with 4. 4 > 3, shift 4.
# Array: [1, 2, 4, 4, 5, 6]
# Compare 3 with 2. 2 < 3, so 3 is in the correct position.
# Array: [1, 2, 3, 4, 5, 6]