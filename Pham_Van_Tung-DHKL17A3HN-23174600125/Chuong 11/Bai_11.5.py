

def nguyen_to(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = []

while True:
        user_input = input("Nhập số (nhấn Enter để kết thúc): ")
        if user_input == "":
            break
        num = int(user_input)
        numbers.append(num)
print("Danh sách số vừa nhập: ", numbers)

so_nguyen_to = [num for num in numbers if nguyen_to(num)]
print("Các số nguyên tố trong danh sách là: ", so_nguyen_to)

so_nguyen_am = [num for num in numbers if num < 0]
so_nguyen_duong = [num for num in numbers if num > 0]

if so_nguyen_am:
    tb_cong_so_am = sum(so_nguyen_am) / len(so_nguyen_to)
    print("Trung bình cộng các phần tử âm: ", tb_cong_so_am)
else:
    print("Không có phần tử âm trong danh sách.")

if so_nguyen_duong:
    tb_cong_so_duong = sum(so_nguyen_duong) / len(so_nguyen_duong)
    print("Trung bình cộng các phần tử dương: ",tb_cong_so_duong)
else:
    print("Không có phần tử dương trong danh sách.")

max_number = max(numbers)
min_number = min(numbers)
print("Giá trị lớn nhất trong danh sách là: ", max_number)
print("Giá trị nhỏ nhất trong danh sách là: ", min_number)

tang_dan = sorted(numbers)
print("Danh sách sau khi được sắp xếp tăng dần là: ", tang_dan)