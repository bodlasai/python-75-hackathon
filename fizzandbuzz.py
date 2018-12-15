for i in range(1,11):
    if(i%3!=0 and i%5!=0):
        print("fizz")
    else:
        if(i%3!=0):
            print(str(i))
        else:
            if(i%5!=0):
                print(str(i))
            else:
                print(i)
