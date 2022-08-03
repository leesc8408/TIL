# https://www.acmicpc.net/problem/23253
import sys
sys.stdin = open('54_자료구조는 정말 최고야.txt')

N, M = map(int, (input().split()))
out = 0

for _ in range(M):
    ki1 = int(input())
    ki2 = list(map(int, input().split()))
    
    for i in range(ki1-1):
        if ki2[i] < ki2[i+1]:
            out = 1
            break
        
print('Yes' if out == 0 else 'No')

