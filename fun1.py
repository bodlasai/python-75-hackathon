#factors of a number using functions
def print_factors(x):
    print("the factors of a num")
    for i in range (1,x+1):
        if(x%i==0):
            print(i)
n=int(input("enter the value"))
print_factors(n) 
