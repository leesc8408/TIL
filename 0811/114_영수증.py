# https://www.acmicpc.net/problem/25304

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/01-ALGORITHM/1회차/이순철/20220811/_영수증.txt')

x = int(input())
n = int(input())
mart_list = [list(map(int, input().split())) for _ in range(n)]
# print(mart_list)
pay = 0

for i in range(n):
    pay += mart_list[i][0] * mart_list[i][1]
# print(x, pay)

if x == pay:
    print('Yes')
else:
    print('No')