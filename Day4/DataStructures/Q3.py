# Count the frequency of each element in a dictionary

d = {"a":1,"b":2,"c":3,"d":1,"e":3}
f={}

for i in d:
    if d[i] in f:
        f[d[i]]+=1
    else:
        f[d[i]]=1

print(f)

l=[1,1,1,2,3,2,3,3,4,4,5,5]
d1={}

for i in l:
    if i in d1:
        d1[i]+=1
    else:
        d1[i]=1
        
        
print(d1)