# https://www.acmicpc.net/problem/2161


n = int(input())
n_list = list(range(1, n+1))
out_list = []
while 1 < len(n_list):
    out_list.append(n_list.pop(0))
    n_list.append(n_list.pop(0))
print(*out_list, *n_list)