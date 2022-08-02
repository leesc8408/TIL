# https://www.acmicpc.net/problem/2953
import sys

sys.stdin = open("30_나는 요리사다.txt")

#입력
li = []
for i in range(1,6):
    score = map(int, input().split())   # 입력값을 줄단위로 받음 

    #연산
    li.append(sum(score))   # 받은 입력값을 합하여 리스트에 추가
    sc_1 = max(li)          # 합산 값이 모은 리스트에서 가장 큰 수를 할당
    no = li.index(sc_1) + 1 # 최대 점수를 이용하여 인덱스 값을 찾고 인덱스는 0부터 시작이라 + 1

#출력
print(f'{no} {sc_1}')   #확인 된 인덱스 값과 최대 점수를 출력   