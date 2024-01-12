from datetime import date

ngay=int(input("Nhập ngày: "))
thang=int(input("Nhập tháng: "))
nam=int(input("Nhập năm: "))
print("Ngày tháng năm vừa nhập là: ", ngay ,"-", thang ,"-", nam)
if (nam % 4 == 0) and (nam % 100 != 0) or (nam % 400 == 0):
    print("Năm", nam, "là năm nhuận ")
    print("Số ngày trong tháng 2 là: 29 ngày")
else:
    print("Năm", nam, "không phải là năm nhuận")
    print("Số ngày trong tháng 2 là: 28 ngày")

cacThu = ["Thứ 2", "Thứ 3", "Thứ 4", "Thứ 5", "Thứ 6", "Thứ 7", "Chủ nhật"]
ngayThangNam = date(nam, thang, ngay)
thu = int(ngayThangNam.strftime('%w'))
print(cacThu[thu - 1])