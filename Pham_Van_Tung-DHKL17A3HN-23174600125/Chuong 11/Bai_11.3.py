ds_thu = ["ant", "bear", "cat", "dog", "elephant", "fish", "goat", "hippo"]
print(ds_thu)
len_thu = len(ds_thu)
print("Number of animal: ", len_thu)
find = str(input("I want to find: "))
tim_kiem = find in ds_thu
if tim_kiem == True:
    print("There is", find, "in list of animals")
else:
    print("There is no", find, "in list of animals")