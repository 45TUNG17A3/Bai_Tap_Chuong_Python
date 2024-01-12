day_so = input("Nhập vào dãy: ")
tach_day_so = day_so.split(" ")
def has_lucky_number(nums):
    for nums in tach_day_so:
        if int(nums) % 7 ==0:
            return True
    return False 
if has_lucky_number(tach_day_so):
    print(True)
else:
    print(False)    
                   