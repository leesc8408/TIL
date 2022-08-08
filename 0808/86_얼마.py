# https://www.acmicpc.net/problem/9325

import sys
sys.stdin = open('_얼마.txt')

t = int(input())
for t_case in range(1, t + 1):

    s = int(input())
    n = int(input())
    if n > 0:
        for _ in range(n):
            q, p = map(int, input().split())
            s += (q * p)
    print(s)