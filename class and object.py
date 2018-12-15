class computer:
    def config(self):
        print("1tb,6gb ram,hello")

a=computer()
#using two class
b=computer()
computer.config(a)
b.config()
