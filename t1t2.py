from sympy import *
r=float(input("input the radius of the circle: "))#task 1
area = r ** 2 * (22 / 7)
print("the area of the circle with radius ", r, " is: ")
print(area)
fn=input("input file name: ")#task 2
f=fn.split(".")
print("extension of the file is: "+f[-1])