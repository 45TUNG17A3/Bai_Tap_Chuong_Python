def nhap_so_nguyen_duong():
    so_lan_lap_lai = 0
    so_cuoi_cung = None

    while True:
        try:
            so = int(input("Nhập số nguyên dương (nhập 0 để kết thúc): "))
            
            if so == 0:
                print("Kết thúc")
                break
            
            if so <= 0:
                raise ValueError("Lỗi số âm.")
            
            if so == so_cuoi_cung:
                so_lan_lap_lai += 1
                if so_lan_lap_lai == 4:
                    raise ValueError("Lỗi nhập lặp lại.")
            else:
                so_lan_lap_lai = 1
            
            so_cuoi_cung = so
        
        except ValueError:
            print("Lỗi nhập số. Hãy nhập lại số nguyên dương.")

if __name__ == "__main__":
    nhap_so_nguyen_duong()