can_nang=float(input("Nhập cân nặng: "))
chieu_cao=float(input("Nhập chiều cao: "))
def tinh_bmi (can_nang, chieu_cao):
    bmi = (can_nang)/(chieu_cao*chieu_cao)
    return bmi
print("bmi =", tinh_bmi(can_nang, chieu_cao))

bmi = tinh_bmi(can_nang, chieu_cao)
if bmi < 18.5:
    print("Gầy")
elif bmi>18.5 or bmi<24.99:
    print("Bình thường")
else:
    print("Thừa cân")