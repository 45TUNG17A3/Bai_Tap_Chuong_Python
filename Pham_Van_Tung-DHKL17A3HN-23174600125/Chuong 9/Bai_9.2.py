can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
n = int(input("Nhập vào năm: "))
def tinh_nam_am_lich (n):
    can_number = n % 10
    chi_number = n % 12
    nam_am_lich = can[can_number] + " " + chi[chi_number]
    return nam_am_lich
print(tinh_nam_am_lich(n))
