# <----- DICTIONARY -----> #

# A dictionary is a collection of key-value pairs
# Dictionaries are defined using curly braces {}
# Dictionaries are mutable
# Dictionaries are heterogeneous
# Dictionaries are ordered
# Dictionaries do not allow duplicate keys

my_dict = {
    "name": "John", 
    "age": 30, 
    "city": "New York"
    }
print(my_dict)
print(type(my_dict))

print(my_dict.items())  # dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])
print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])
print(my_dict.values())  # dict_values(['John', 30, 'New York'])
print(my_dict.get("name"))  # John
print(my_dict.get("marks"))  # None

# my_dict.update({"marks": 90})
# print(my_dict)  # {'name': 'John', 'age': 30, 'city': 'New York', 'marks': 90}
# print(my_dict.fromkeys(["name", "age", "city"]))  # {'name': None, 'age': None, 'city': None}
# my_dict.pop("name")  # Remove the key-value pair from the dictionary
# print(my_dict)  # {'age': 30, 'city': 'New York', 'marks': 90}
# my_dict.popitem()  # Remove the last key-value pair from the dictionary
# print(my_dict)  # {'age': 30, 'city': 'New York'}

for i in  my_dict.values():
    print(i)
    