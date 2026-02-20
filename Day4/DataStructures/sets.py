# <----- SETS -----> #
# A set is a collection of unique items
# Sets are defined using curly braces {}
# Sets are mutable
# Sets are heterogeneous
# Sets are unordered
# Sets do not allow duplicate values

my_set = {1,2,3,4,5 ,"helllo", 3.14}
# print(my_set)
# print(type(my_set))

# # Empty set
# # empty_set = set()
# # print(empty_set)
# # print(type(empty_set))

# my_set.add(123)  # Add the value into the set at end
# print(my_set)   #{1, 2, 3, 4, 5, 'helllo', 3.14, 123}

# my_set.remove(1)  # Remove the value from the set
# print(my_set)   #{2, 3, 4, 5, 'helllo', 3.14, 123}

# my_set.discard(5)  # Remove the value from the set
# print(my_set)   #{2, 3, 4, 'helllo', 3.14, 123}

# my_set.pop()  # Remove the value from the set
# print(my_set)   #{2, 3, 4, 'helllo', 3.14}

# # my_set.clear()  # Remove all the values from the set
# # print(my_set)   #{}

# my_set.update({99,10})  # Add the values into the set at end
# print(my_set)   #{2, 3, 4, 'helllo', 3.14, 99, 10}

# print(dir(my_set))

# OPERATIONS ON SETS
# UNION
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))  # {1, 2, 3, 4, 5, 6, 7, 8}
print(s1 | s2)  # {1, 2, 3, 4, 5, 6, 7, 8}

# INTERSECTION
print(s1.intersection(s2))  # {4, 5}
print(s1 & s2)  # {4, 5}

# DIFFERENCE =>  
print(s1.difference(s2))  # {1, 2, 3}
print(s1 - s2)  # {1, 2, 3}

# SYMMETRIC DIFFERENCE
print(s1.symmetric_difference(s2))  # {1, 2, 3, 6, 7, 8}
print(s1 ^ s2)  # {1, 2, 3, 6, 7, 8}