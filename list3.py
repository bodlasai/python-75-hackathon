#to draw graphs in python console

import matplotlib.pyplot as plt
plt.plot([1,2,3,4],'ro')
plt.ylabel("hello")
plt.xlabel("hai")
e=[100,200,300,400,500,600,123,435,223,112,112,334,555,3,4499,99,90,90]
y=[]
for i in range(len(e)):
    y.append(5)
    
plt.plot(e,y,'bs')
