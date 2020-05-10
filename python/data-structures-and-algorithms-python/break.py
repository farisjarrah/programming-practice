data1 = [3,6,9,12,15,18,21,24,27,30]
target1 = 27

def in_data(data, target):
    for item in data:
        if item == target:
            found = True
            return True
            break
    else:
        return f"{target} is not in the data set"

print(in_data(data1, target1))
