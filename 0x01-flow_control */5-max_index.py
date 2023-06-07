Lst = [1, 15, 2, 38, 48, 7, 16, 44]

max_num = Lst[0]  

max_index = 0    

for i in range(1, len(Lst)):

    if Lst[i] > max_num:

        max_num = Lst[i]

        max_index = i

print("Max is", max_num, "at index", max_index)

