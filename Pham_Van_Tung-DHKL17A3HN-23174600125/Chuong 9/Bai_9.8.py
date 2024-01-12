def kiemtraHoanHao(n):
    tong = 0
    for i in range(1, n):
        if (n % i) == 0:
            tong += i
            
    if tong == n:
        return True
    else:
        return False


n = int(input("Nhập vào số nguyên n: "))
if kiemtraHoanHao(n) == True:
    print(n, ' la so hoan hao')
else:
    print(n, ' không la so hoan hao')