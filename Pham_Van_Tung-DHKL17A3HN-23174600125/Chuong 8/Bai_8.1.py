a=int(input("Nhập số a:"))
b=int(input("Nhập số b:"))
c=int(input("Nhập số c:"))
d=int(input("Nhập số d:"))
max = a
if max < b:
    max = b
if max < c:
    max = c
if max < d:
    max = d
print("Max =", max)    
min = a
if min > b:
    min = b
if min > c:
    min = c
if min > d:
    min = d
print("Min =", min)              