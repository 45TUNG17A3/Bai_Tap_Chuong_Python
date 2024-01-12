tien_muon_doi = float(input("Số tiền muốn đổi: "))
so_to_500k = tien_muon_doi//500000
print("Số tờ 500000: ", so_to_500k)
so_to_200k = (tien_muon_doi-so_to_500k*500000)//200000
print("Số tờ 200000: ", so_to_200k)
so_to_100k = (tien_muon_doi-so_to_500k*500000-so_to_200k*200000)//100000
print("Số tờ 100000: ", so_to_100k)
so_to_50k = (tien_muon_doi-so_to_500k*500000-so_to_200k*200000-so_to_100k*100000)//50000
print("Số tờ 50000: ", so_to_50k)
tien_con_lai = (tien_muon_doi-so_to_500k*500000-so_to_200k*200000-so_to_100k*100000-so_to_50k*50000)
print("Tiền còn lại: ", tien_con_lai)