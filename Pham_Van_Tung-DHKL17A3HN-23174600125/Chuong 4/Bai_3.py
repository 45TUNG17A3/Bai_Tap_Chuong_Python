x = int(input("Nhập vào số tự nhiên X: "))
y = int(input("Nhập vào số tự nhiên Y: "))
if x<y:
    print("Các giá trị chia hết cho ", x, "là: ")
    for gia_tri in range(1,y+ 1):
        if gia_tri%x==0:
            print(gia_tri)
            