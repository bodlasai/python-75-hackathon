import random
for x in range(1,10):
    print (random.randint(1,101))
print("function on random numbers")
print(random.choice([10,20,30,10]))
print(random.randrange(20, 50))

a=[1,2,3,4,5]
random.shuffle(a)
for i in range(0,len(a)):
    print(a[i])

print(random.uniform(2,5))
