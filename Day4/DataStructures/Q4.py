# Sum of values of two dictionaries

d1 ={
    "a":1,
    "b":2,
    "c":3
}

d2 ={
    "a":4,
    "b":5,
    "c":6
}
d3 = {}

for i in d1:
    if i in d2:
        d3[i] = d1[i] + d2[i]
    
print(d3)