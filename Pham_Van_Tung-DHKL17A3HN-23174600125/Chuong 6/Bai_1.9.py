lai_suat = float(input("Lãi suất 1 năm (%): "))
so_tien_gui = float(input("Số tiền gửi: "))
so_thang_gui = int(input("Số tháng gửi: "))
tien_lai = ((so_tien_gui * so_thang_gui/12) * (lai_suat))/100
print("Tiền lãi = ", tien_lai)
von_va_lai = so_tien_gui + tien_lai
print("Tiền vốn + lãi = ", so_tien_gui, "+", tien_lai, "=", von_va_lai)