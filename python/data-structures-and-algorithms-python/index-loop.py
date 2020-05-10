a = [2,4,6,8,10,12,14,16,18,20]
big_index = 0
for j in range(len(a)):
    if a[j] > a[big_index]:
        big_index = j

print(big_index)
