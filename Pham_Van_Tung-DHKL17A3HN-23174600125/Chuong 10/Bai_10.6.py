import math
a = int(input("Nhập vào a: "))
b = int(input("Nhập vào b: "))
c = int(input("Nhập vào c: "))
if a == 0:
    print("Phương trình có nghiệm duy nhất x=", (-c/b))
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b+math.sqrt(delta))/(2*a)
        x2 = (-b-math.sqrt(delta))/(2*a)
        print("Phương trình có hai nghiệm phân biệt x1 = ", x1, " và x2 = ", x2)
    elif delta == 0:
        print("Phương trình có nghiệm kép x1 = x2 =", (-b)/(2*a))
    else:
        print("Phương trình vô nghiệm")