first={
    "name":"sai",
    "college":"sathyabama",
    "present year":"3rd",
    "pgm":"B.E-CSE"
}
#to display all the values
for x,y in first.items():
    print(x,y)
#chaniging the value
first["name"]="ram"
print(first)
#printing the terms
for x in first:
    print(x)
#printing the values
for x in first.values():
    print(x)
#printing the length
print(len(first))
#pop(means remove)
first.pop("pgm")
print(first)
#popitem
first.popitem()
print(first)
#can use del too
del first["college"]
print(first)
