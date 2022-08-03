# https://www.acmicpc.net/problem/2750

# n개의 수를 heapq 리스트에 담는다
# 리스트의 값을 heappop(리스트[0])으로 최소값을 빈 리스트에 담는다
# while 로 반복 heapq 리스트에 값이 없을때까지
import heapq
import sys
sys.stdin = open('64_수 정렬하기.txt')

# t = int(input())
# n_list = []

# for _ in range(t):
#     n_list.append(int(input()))
# n_list.sort()
# print(*n_list, sep='\n')

t = int(input())
n_list = []

for _ in range(t):
    n = (int(input()))
    heapq.heappush(n_list, n)
    print(n_list)
for _ in range(t):
    print(heapq.heappop(n_list))