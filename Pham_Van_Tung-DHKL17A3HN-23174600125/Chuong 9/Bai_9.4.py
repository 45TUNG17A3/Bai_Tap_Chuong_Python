import math
x = float(input("Nhập vào x: "))
n = float(input("Nhập vào n: "))
def tinh_S(n, x):
    S = math.pow((math.pow(x,2)+1), n)
    return S
print("Gía trị trả về là",tinh_S(n, x))