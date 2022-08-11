# https://www.acmicpc.net/problem/2606

from pprint import pprint
import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/01-ALGORITHM/1회차/이순철/20220810/_바이러스.txt')

n = int(input())
m = int(input())
g_list = [[] for _ in range(n + 1)]
visit = [False] * (n + 1)
cnt = 0

for _ in range(m):
    p1, p2 = map(int, input().split())
    g_list[p1].append(p2)
    g_list[p2].append(p1)
# print(*g_list, sep='\n')  인접 리스트 생성 확인
# print(visit)              방문 리스트 확인(인접 리스트와 인덱스 길이 일치 확인)
com = 1
com_stack = [com]
# 스택 리스트 
visit[com] = True
# 시작점 방문
# print(com_stack)
while com_stack:
# 스택에 모든 값이 pop될 때까지 반복
    com = com_stack.pop()
    # 현재는 com = 1 이었으므로 1이 pop
    for j in g_list[com]:
    # 인접 리스트 인덱스[1] 값 [2,5] 
        if not visit[j]:
        # 방문[2]인덱스가 not True(=False)이면 다음 코드
            visit[j] = True
            # 방문[2]인덱스 값을 True로 할당
            com_stack.append(j)
            # 스택에 2를 append하여 쌓는다
        # print(visit)
    print(com)
    print(com_stack)
    
# print(visit.count(True) - 1)   
# 시작점을 제외하면 답이 나옴 