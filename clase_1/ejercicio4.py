import math
print("Formula General")
a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
c = int(input("Valor de c: "))
#a = 2
#b = 4
#c = -6

x1 = (-b+(b**2-(4*a*c))**.5)/(2*a)
x2 = (-b-(b**2-(4*a*c))**.5)/(2*a)

print("X1 = ", x1)
print("X2 = ", x2)