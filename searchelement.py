from array import *

arr= array('i',[])

n=int(input("enter the n value"))

for i in range(n):
    x=int(input("enter the values"))
    arr.append(x)

print(arr)

vals=int(input("enter the element to search"))
k=0
for e in arr:
    if e==vals:
        print(k)
        break
    k=k+1
