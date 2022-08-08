# https://www.acmicpc.net/problem/5800

import sys
sys.stdin = open('_성적 통계.txt')

k = int(input())
for x in range(1, k + 1):
    c_s = list(map(int, input().split()))
    c = c_s.pop(0)
    # print(c)
    # print(c_s)
    rev_c_s  = sorted(c_s, reverse=True)
    # print(rev_c_s)
    gap = [rev_c_s[i] - rev_c_s[i + 1] for i in range(c - 1)]
    
    print(f'Class {x}')
    print(f'Max {max(c_s)}, Min {min(c_s)}, Largest gap {max(gap)}')
