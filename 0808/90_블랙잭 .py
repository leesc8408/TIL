# https://www.acmicpc.net/problem/2798

import sys
sys.stdin = open('_블랙잭 .txt')

n, m = map(int, input().split())
cards = list(map(int, input().split()))
# print(n, m)
# print(cards)
cnt = []

for i1 in range(n):
    for i2 in range(i1+1, n):
        for i3 in range(i2+1, n):
            score = cards[i1] + cards[i2] + cards[i3]
            if m >= score:
                cnt.append(score)
print(max(cnt))
            
