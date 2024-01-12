x = int(input("Nhập vào x: "))
n = int(input("Nhập vào n: "))
def tinh_A(n, x):
    A=(x**2 + x + 1)**n + (x**2 - x + 1)**n
    return A
print("Gía trị là: ", tinh_A(n,x))