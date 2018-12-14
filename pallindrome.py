#checking pallindrome or not
    
a=str(input("enter the string:"))    
print("reverse the string")
print(a[::-1])
r=(a[::-1])
if(a==r):
    print("pallindrome")
else:
    print("not a pallindrome")
