f= lambda a:a*a
result=f(5)
print(result)
#adding three numbers
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
#another way of passing two values

def ok(n):
  return   lambda  a:a*n

result=ok(2)
print(result(14
