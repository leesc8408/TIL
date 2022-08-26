# https://www.acmicpc.net/problem/10816

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/TIL/0728/_숫자 카드 2.txt')

n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
n_dict ={}

for i in range(n):
    if n_list[i] not in n_dict.keys():
        n_dict[n_list[i]] = 1
    else:
        n_dict[n_list[i]] += 1
for j in m_list:
    if j in n_dict.keys():
        print(n_dict[j],end=' ')
    else:
        print('0', end=' ')
