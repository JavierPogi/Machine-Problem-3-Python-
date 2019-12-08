import numpy as np

x = input("Input all your x-values: ").split(" ")
y = input("Input all your y-values: ").split(" ")
#Will take an infinite amount of inputs, seperated by spaces
#Will turn the inputted values, into a list
x = np.array(x,dtype=float)
y = np.array(y,dtype=float)
#Turns the list of inputs into an nx1 array
if len(x) >= 10:
    l = 10
    for i in range(1,10):
        pol = np.polyfit(x,y,i)
        val = np.polyval(pol,x)
        nor = np.linalg.norm(y-val)
        z=nor.argmin()
        coeff = np.polyfit(x,y,z)
        #Least norm error vector process
else:
    l = len(x) - 1

    for i in range(1,l):
        pol = np.polyfit(x,y,i)
        val = np.polyval(pol,x)
        nor = np.linalg.norm(y-val)
        z=nor.argmin()
        coeff = np.polyfit(x,y,z)
        #Least norm error vector process
print("Your coefficient/s are: ", coeff)
print("According to the norm(Approximated value): ", z)


    