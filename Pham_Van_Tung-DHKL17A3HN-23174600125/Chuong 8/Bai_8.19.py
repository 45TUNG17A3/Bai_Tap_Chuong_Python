# def dao_nguoc_day_so(n):
#     day_so = list(range(1, n+1))
#     day_so_le = [x for x in day_so if x % 2 != 0]
#     day_so_dao_nguoc = day_so_le[::-1]
#     return day_so_dao_nguoc

# so_luong = int(input("Nhập số lượng số trong dãy: "))
# ket_qua = dao_nguoc_day_so(so_luong)
# print("Dãy số đảo ngược và chỉ hiển thị số lẻ:", ket_qua)

chuoi = str(input("Nhập vào chuỗi: "))
tach_chuoi = chuoi.split(" ")
chuoi_moi = []
for item in tach_chuoi:
    if int(item)%2!=0:
        
        chuoi_moi.append(item)
chuoi_moi = chuoi_moi[::-1]
for item in chuoi_moi:
    print(item, end = " ")