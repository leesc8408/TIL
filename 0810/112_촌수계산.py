# https://www.acmicpc.net/problem/2644

import sys
sys.stdin = open('_촌수계산.txt')

n = int(input())
x, y = map(int, input().split())
m = int(input())
family_ = [[] for _ in range(n + 1)]

for _ in range(m):
    p1, p2 = map(int, input().split())
    family_[p1].append(p2)
    family_[p2].append(p1)
# print(*family_, sep='\n')  # 인접 리스트 생성 확인

visit = [0] * (n + 1)   # 이동 리스트
f_stack = [x]   # 스택 리스트 

while f_stack:
    dx = f_stack.pop()
    # 최근 입력 된 정점
    for j in family_[dx]:
    # 해당 정점에 인접 리스트에서 있는 인접 정점으로 반복문 
        if visit[j] == 0:   
        # 해당 정점 인덱스를 가진 이동 리스트에 처음 방문 이면
            visit[j] = visit[dx] + 1
            # 이전 정점의 이동 횟수 +1을 할당
            # 이렇게 하면 시작 점에서 1번 이동한 정점들의 이동리스트 값이 1로 누적 
            # 그 정점들의 인접 리스트에 있는 다른 정점에 이동 할때는 1에 +1로 누적하여 2로 누적되게 된다.
            f_stack.append(j)
            # 정점들을 다시 스택에 쌓는다
            # print(visit)
# 스택에 값이 없으면 종료
# 현대 이동 리스트의 값 [0, 2, 1, 3, 0, 0, 0, 2, 2, 2]
# 0인 인덱스는 기준 인덱스(정점)에서 이동이 불가한 인덱스(정점)

print(visit[y] if visit[y] > 0 else -1)
# 이동 횟수는 촌수가 되므로 촌수를 못세는 0인 경우는 -1이 출력 되도록 조건문 설정