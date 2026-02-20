# <---- TUPLE ----> #

# tuple => data structure , heterogeneous , immutable , ordered
# duplicate values are allowed

t = (10, 20, True, "hello")
print(t)
print(type(t))
print(len(t))
print(t[2])

# immutable => cannot change the value
# t[2] = 300
# print(t)  # TypeError: 'tuple' object does not support item assignment

# t.append(20)
# print(t)  # AttributeError: 'tuple' object has no attribute 'append'

print(t.count(20))  # 1
print(t.index("hello"))  # 3

# print(max(t))  # 20
# print(min(t))  # 10

# t2 = (1,)  # tuple
# print(type(t2))  # tuple


t3 = (1, 2, 3)
a, b, c = t3  # unpacking the tuple into variables
# print(a)  # a=1
# print(b)  # b=2
# print(c)  # c=3
# print(t3)

# Membership operators
print(1 in t3)  # True
print(4 in t3)  # False
print(5 not in t3)  #True

