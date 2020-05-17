data = [2, 3, 4, 5, 6, 7, 9, 2, 6, 2]
target = 2

def count(data, target):
    n = 0
    for item in data:
        if item == target:
            print(f"{item} is target")
            n += 1
        else:
            print(f"{item} is not target")
    return n

print(count(data, target))
