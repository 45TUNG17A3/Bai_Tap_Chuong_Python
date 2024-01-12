#Bài tập 1
#1.1
print("**  ** ****** **     **     ** ****")
print("**  ** **     **     **     **   **")
print("****** *****  **     **     **   **")
print("**  ** **     **     **     **   **")
print("**  ** ****** ****** ****** ** ****")
#1.2
x=10
y=5
tong=x+y
hieu=x-y
tich=x*y
thuong=x/y

print('KET QUA CAC PHEP TINH LA:')
print("Tong cua ",x,'+',y, '=', tong)
print("Hieu cua ",x,'-',y, '=', hieu)
print("Tich cua ",x,'*',y, '=', tich)
print("Thuong cua ",x,'/',y, '=', thuong)
#1.3
ten_hang="Sữa hộp Vinamilk"
so_luong=5
don_gia=25000
tien_phai_tra=so_luong*don_gia
print("Tên hàng:",ten_hang)
print("Số lượng",so_luong)
print("Tiền phải trả",tien_phai_tra)
#1.4
import math
a = float(input("Nhập độ dài cạnh a ="))
b = float(input("Nhập độ dài cạnh b ="))
c = float(input("Nhập độ dài cạnh c ="))
p = (a + b + c)/2
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác =",S)
