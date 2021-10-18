import cmath

a = float(input("Enter a Number: "))
b = float(input("Enter a Number: "))
c = float(input("Enter a Number: "))

d = (b**2)-(4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solutions of {0} and {1} are: ".format(sol1,sol2))

