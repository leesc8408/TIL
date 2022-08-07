# https://www.acmicpc.net/problem/2711

import sys
sys.stdin = open('38_오타맨 고창영.txt')
t = int(input())
for t_case in range(1, t + 1):
    n, m = input().split()
    n = int(n)
    m = list(m)
    # print(n,m,type(n))
    m.pop(n-1)
    print(''.join(m))