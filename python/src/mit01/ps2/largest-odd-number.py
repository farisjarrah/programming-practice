a=1
b=2
c=3

def largest_odd(x,y,z):
    if x%2==0 and y%2==0 and z%2==0:
        return "All numbers are even"
    elif x==y and z==x:
        return f"All numbers are the same: {x}"
    else:
        num_list=[x,y,z]
        largest_item=0
        for i in num_list:
            if i%2==0:
                continue
            else:
                if largest_item>i:
                    largest_item=i
    return largest_item

print(largest_odd(2,2,2))
print(largest_odd(3,5,7))
print(largest_odd(3,3,3))
