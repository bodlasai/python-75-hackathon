import  classandobject

a=int(input("entert the a value"))
b=int(input("enter the b value"))

c=classandobject.add(a,b)
print(c)
d=classandobject.sub(a,b)
print(d)
e=classandobject.mul(a,b)
print(e)
f=classandobject.div(a,b)
print(f)

#crete seperate file for the follwing
class computer:
    def config(self):
        print("1tb,6gb ram,hello")

a=computer()
computer.config(a)
a.config()
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
