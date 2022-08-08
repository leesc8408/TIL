# https://www.acmicpc.net/problem/11170

import sys
sys.stdin = open('_0의 개수.txt')

t = int(input())
for t_case in range(t):
    n, m = map(int, input().split())
    cnt_0 = 0

    for i in range(n, m+1):
        for j in str(i):
            if j == '0':
                cnt_0 += 1
    print(cnt_0)