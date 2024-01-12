alice_candies = int(input("Nhập số kẹo của Alice: "))
bob_candies = int(input("Nhập số kẹo của Bob: "))
carol_candies = int(input("Nhập số kẹo của Carol: "))
print("Số viên kẹo dư phải đập là: ", (alice_candies + bob_candies + carol_candies)%3)