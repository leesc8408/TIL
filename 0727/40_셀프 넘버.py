# https://www.acmicpc.net/problem/4673
d_list = []
all_list = []
for n in range(1,10001):
    all_list.append(n)
    n_str = str(n)
    d = n
    for i in range(len(n_str)):
        d += int(n_str[i])
    d_list.append(d)    
# print(all_list)
out = set(all_list) - set(d_list)
print(*sorted(out), sep='\n')
