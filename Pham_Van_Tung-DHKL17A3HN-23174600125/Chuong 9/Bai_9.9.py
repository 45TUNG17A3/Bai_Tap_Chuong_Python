import math 
r = float(input("Nhập bán kính: "))
def tinh_S_hinh_tron(r):
    dien_tich = math.pi*(math.pow(r, 2))
    return dien_tich
def tinh_P_hinh_tron(r):
    chu_vi = math.pi*(r*2)
    return chu_vi
a = float(input("Nhập cạnh hcn: "))
b = float(input("Nhập cạnh hcn: "))
print("Diện tích hình tròn là:", tinh_S_hinh_tron(r))
print("Chu vi hình tròn là: ", tinh_P_hinh_tron(r))
def tinh_S_hcn(a, b):
    dien_tich = a*b
    return dien_tich
def tinh_P_hcn(a, b):
    chu_vi = (a+b)*2
    return chu_vi
print("Diện tích hình chữ nhật là: ", tinh_S_hcn(a, b))
print("Chu vi hình chữ nhật là: ", tinh_P_hcn(a, b))
