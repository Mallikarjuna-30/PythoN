# Write a python code to for union of two dictionary

d1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

d2 = {
    "naam": "Jane",
    "agge": 25,
    "citty": "Los Angeles"
}
d3 = {}
# d1.update(d2)

for i in d1:
    d3[i]=d1[i]
for i in d2:
    d3[i]=d2[i]
    
print(d3)