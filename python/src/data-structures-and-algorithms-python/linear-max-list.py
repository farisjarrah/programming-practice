list1 = [4,17,23,8,3,44]
biggest = list1[0]
littlest = list1[0]
for thing in list1:
    if thing > biggest:
        biggest = thing
    if thing < littlest:
        littlest = thing

print(littlest)
print(biggest)
