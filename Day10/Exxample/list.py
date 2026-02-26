# Example

l = [1,2,3,4,"ASK"]

# for i in range(3):
#     item = int(input("Enter an ele : "))
#     l.append(item)
    
# l.remove(1)
# l.insert(2,3232)
# print(l)
# print(len(l))
# n = len(l)
# i = n-1
# while i >= 0:
#     print(l[i],end=" , ")
#     i = i-1
    
st = 0
last = len(l) - 1

while st<last:
    l[st],l[last] = l[last],l[st]
    st = st+1
    last = last-1
print(l)