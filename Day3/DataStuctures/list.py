# <----- LIST -----> #

# list => data structure , heterogeneous , mutable , ordered
# list <=> array
# elements in list can be accessed by index
# list is dynamic => add/remove values
# duplicate values are allowed

# l = [1, 2.02, 3, 4, 4, "hello", True]
# print(l)
# print(type(l))  # class 'list'
# print(len(l))  # 7
# print(l[3])  # 4    Index starts from 0

# # mutable => change the value
# l[3] = 34
# print(l)  # [1, 2.02, 3, 34, 4, 'hello', True]

# # negative indexing
# print(l[-1])  # True
# print(l[-2])  # hello

# # slicing
# print(l[0:2])  # [1, 2.02]
# print(l[-4:0:-1])  # [34, 3, 2.02]

# l.append("HIIII")
# print(l)  # [1, 2.02, 3, 34, 4, 'hello', True, 'HIIII']

# l.remove("hello")
# print(l)  # [1, 2.02, 3, 34, 4, True, 'HIIII']

# l.pop()  # we can even pass index
# print(l)  # [1, 2.02, 3, 34, 4, True]

# l.insert(2, "HII")
# print(l)  # [1, 2.02, 'HII', 3, 34, 4, True]

# l.extend([3, 5, 74, 32])
# print(l)  # [1, 2.02, 'HII', 3, 34, 4, True, 3, 5, 74, 32]

# print(l.count(3))  # 2

# print(l.index(34))  # 4

# l.sort()  # ascending order
# print(l)  # [1, 2.02, 'HII', 3, 34, 4, True, 3, 5, 74, 32]

# l.sort(reverse=True)  # descending order  or we can use l.reverse()
# print(l)  # [74, 32, 5, 4, 3, 3, 'HII', True, 34, 2.02, 1]

# help(l)


nums = [10, 20, 30, 40, 50]
b = nums.copy()
b[1] = 200
print(b)
print(nums)


for i in nums:
    print(i, end=" ")
