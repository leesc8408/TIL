# https://www.acmicpc.net/problem/11286

# x != 0이면 비어있는 배열에 x를 추가, x=0이면 배열에서 가장 작은값이 출력 후 삭제

import heapq
import sys
input = sys.stdin.readline

t = int(input())

bea_ = []

for _ in range(t):
    x =int(input())
    if x != 0:                              # 입력값이 0이 아닐경우
        heapq.heappush(bea_, (abs(x), x))   # 힙푸쉬로 bea_리스트 추가함, 
    else:                                   # 추가할때 절대값과 입력값을 튜플로 지정하여 입력
        if len(bea_) == 0:                  # 리스트의 값의 개수가 없으면 0 출력
            print('0')
        else:
            print(heapq.heappop(bea_)[1])   # 힙팝으로 절대값중 가장 작은값의 튜플의 두번째 인덱스 값을 출력