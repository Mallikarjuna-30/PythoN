# sum of all values in a dictionary

d1={
    "a":1,
    "b":2,
    "c":3,
    "d":4,
    "e":5
}

sum=0
for i  in d1.values():
    sum+=i

print(sum)