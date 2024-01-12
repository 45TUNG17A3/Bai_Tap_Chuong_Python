import math
n = int(input("Nhập n: "))
x= float(input("Nhập x: "))
A = pow((x*x + x +1), n) + pow((x*x - x + 1), n)
print("A=(x*x + x + 1)^n + (x*x - x + 1)^n = ", A)