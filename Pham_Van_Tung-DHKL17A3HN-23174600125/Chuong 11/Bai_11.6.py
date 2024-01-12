list = [74,74,72,72,73,69,69,71,76,71]
list_moi = []
for item in list:
    doi_met = item * (1/0.0254)
    list_moi.append(doi_met)
print("Kết quả đổi inch sang mét là: ")    
for item in list_moi:
    print(item, end = " ") 
print("\nBa giá trị đầu tiên là: ",list_moi[0:3])
print("Ba giá trị cuối cùng là: ", list_moi[-3:])   
 
trung_binh = (sum(list_moi)/len(list_moi))
print("Trung bình cộng là: ", trung_binh)
chieu_cao_max = max(list_moi)
print("Chiều cao lớn nhất là: ", chieu_cao_max)
chieu_cao_min = min(list_moi)
print("Chiều cao nhỏ nhất là: ", chieu_cao_min)
list_moi.sort()
print("Sắp xếp tăng dần là: ",list_moi)
list_moi.sort()
list_moi.reverse()
print("Sắp xếp giảm dần là: ", list_moi)