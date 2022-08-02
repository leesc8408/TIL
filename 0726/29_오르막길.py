# https://www.acmicpc.net/problem/2846
from audioop import reverse
import sys

sys.stdin = open("29_오르막길.txt")
#입력
t = int(input())
num = list(map(int, input().split()))
im = 0
high = []

#연산
for i in range(t - 1):
    if num[i] < num[i+1]:       # 지금 위치의 수와 다음 수를 비교
        im += num[i + 1] - num[i]   # 비교한 수 중 큰데서 작은걸 빼서 누적수 im에 할당      
        high.append(im)             # 리스트에 수를 추가
    else:
        high.append(im)     # 비교 시 다음 나올 수가 지금 부터다 작다면 현재 할당값 리스트로 보냄
        im = 0      # 누적 수 초기화

#출력   
print(sorted(high, reverse=True)[0])    # 모여진 누적수 값을 정렬하고 리버스로 역순정렬 후 [0] 값을 출력