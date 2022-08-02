import sys

sys.stdin = open("35_덩치.txt")

# 강사님 풀이
t = int(input())
xy_list = []

for i in range(t):
    x, y = list(map(int, input().split()))
    xy_list.append((x, y))    
# print(hum)
rank = [0] * t

for a in range(t):
    A = xy_list[a]
    for b in range(t):
        B = xy_list[b]
        if A[0] > B[0] and A[1] > B[1]:
            rank[b] += 1
for ranks in rank:
    print(ranks + 1, end=' ')