a = float(input("Nhập vào giá trị của a: "))
b = float(input("Nhập vào giá trị của b: "))

x = a
y = b

tich = a * b

while a * b != 0:
    if a > b:
        a = a % b
    else:
        b %= a
ucln = a + b
bcnn = tich / ucln
print("Bội chung nhỏ nhất của ", x, " và ", y, " là: ", bcnn)