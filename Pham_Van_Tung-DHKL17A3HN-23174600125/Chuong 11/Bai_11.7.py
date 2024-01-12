danh_sach = str(input("Nhập vào danh sách: "))
tach_ds = danh_sach.split(" ")
day_moi = []
thresh = int(input("Nhập vào một giá trị: "))
for item in tach_ds:
    if (int(item)) <= (thresh):
        ket_qua = False
    else:
        ket_qua = True
    day_moi.append(ket_qua)            
for item in day_moi:
       print(item, end =" ")   