def nhap_so():
    danh_sach =[]
    tiep_tuc = 1
    sum = 0

   
    while tiep_tuc == 1:
        so = int(input("Nhập giá trị: "))
        tiep_tuc = int(input("Tiếp tục nhập giá trị? 1: Có, 0: không "))
        danh_sach.append(so)
        sum = sum + so
    for item in danh_sach:
        print(item, end = " ")
    print("")
    print("Tổng của dãy số là: ", sum)
    x = int(input("Nhập vào x: "))
    dem_so = danh_sach.count(x)
    print("Số ", x, " xuất hiện ",dem_so, " lần")
    if all(item < x for item in danh_sach):
        print("Số", x, "lớn hơn tất cả các số trong list")
    else:
        print("Số", x, "không lớn hơn tất cả các số trong list")
        print("Các số lớn hơn", x,"trong list là:")   
        day_so_lon = []
        for item in danh_sach:
            if item > x:
                day_so_lon.append(item)
        for item in day_so_lon:
             print(item, end = " ")
        
nhap_so()
