def kiem_tra_tam_giac(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Độ dài cạnh phải là số dương và khác 0.")
    elif a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba cạnh nhập vào không thỏa mãn điều kiện tồn tại tam giác.")
    else:
        print("Đây là tam giác.")

def nhap_do_dai_canh():
    try:
        a = float(input("Nhập độ dài cạnh a: "))
        b = float(input("Nhập độ dài cạnh b: "))
        c = float(input("Nhập độ dài cạnh c: "))
        
        kiem_tra_tam_giac(a, b, c)
        
    except ValueError as ve:
        print("Lỗi: ", ve)
    except Exception as e:
        print("Lỗi: ", e)

nhap_do_dai_canh()        