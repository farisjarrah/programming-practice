a=2
b=4
c=6
d=8
e=10
f=12
g=14
h=16
i=18
j=20

def largest_odd_integer(a,b,c,d,e,f,g,h,i,j):
    int_list=[a,b,c,d,e,f,g,h,i,j]
    high = 0
    for x in int_list:
        if x%2==0:
            even_list.append(x)
        else:
            if x>high:
                high=x
    if len(even_list) == len(int_list):
        return "There was no odd numbers"

    return high

print(largest_odd_integer(2,2,2,2,2,2,2,2,2,2))
print(largest_odd_integer(1,2,3,4,5,6,7,8,9,10))
print(largest_odd_integer(3,6,9,12,15,18,21,24,27,30))
print(largest_odd_integer(9,8,7,6,5,4,3,2,1,0))
print(largest_odd_integer(1,1,1,1,1,1,1,1,1,1))
print(largest_odd_integer(-12,-9,-7,-5,-3,0,3,6,9,12))
