x = 5

def fun():
    x = 10
    print("local value", x)

fun()
print("global value", x)
