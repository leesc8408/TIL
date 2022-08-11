# https://www.acmicpc.net/problem/17388

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/01-ALGORITHM/1회차/이순철/20220811/_와글와글 숭고한.txt')

total = list(map(int, input().split()))
university = ['Soongsil', 'Korea', 'Hanyang']
# print(total)
if sum(total) >= 100:
    print('OK')
else:
    print(university[total.index(min(total))])