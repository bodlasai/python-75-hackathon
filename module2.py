import connect

t=int(input("enter the t value"))

c=connect.play(t)
print(c)
#cretae seperate file for and name it as coonect
def play(t):

    for i in range(1,t+1):
        n=int(input("enter the n value"))
        n1=0;
        n2=0;
        n3=0;
        n1=n/3
        n1=3*n1*(n1+1)/2
        n2=n/5-1
        n2=5*n2*(n2+1)/2
        n3=n/15
        n3=15*n3*(n3+1)/2
        return (n1+n2-n3)
