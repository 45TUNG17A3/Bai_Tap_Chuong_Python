import math
x = float(input("Nhập vào x: "))
n = float(input("Nhập vào n: "))
S = (math.pow((math.pow(x,2)+x+1),n)) + (math.pow((math.pow(x,2)-x+1),n))
print("Giá trị của S là: ", S)