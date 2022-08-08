# https://www.acmicpc.net/problem/1453

import sys
sys.stdin = open('_피시방 알바.txt')

t = int(input())
n = list(input().split())
n_list ={}

for i in n:
    if i not in n_list.keys():
        n_list[i] = 0
    else:
        n_list[i] += 1

print(n_list.items())
print(sum(list(n_list.values())))

