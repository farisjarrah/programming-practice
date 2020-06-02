s='2.2,2.2,2.2,2.2'
separator=','
index_list=[]

for x in range(0, len(s)):
    if s[x] == separator:
        index_list.append(x)

second_index=index_list[1]
last_index=index_list[0]
total_sum=0

for x in index_list:
    if x==index_list[0]:
        total_sum=float(s[0:x]) + float(s[x+1:second_index])
    elif x==index_list[-1]:
        total_sum=total_sum+float(s[x+1:])
        break
    else:
        total_sum=total_sum+float(s[last_index+1:x])
        last_index=x

print(total_sum)
