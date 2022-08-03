# https://www.acmicpc.net/problem/1236

# 입력 n=행, m=열  n,m <= 50 
# 다음 줄 부터 n개 줄에 상태 
# .은 빈칸 X는 경비원  
# 출력 = 추가할 경비원수
# 요구사항 : 행 또는 열에 최소 1명 이상의 경비

from pprint import pprint 
import sys
sys.stdin = open('69_성 지키기.txt')

n, m = map(int, input().split())
castle = [list(input()) for _ in range(n)]
cnt_n = 0               # 행에 경비가 없을때 카운트
cnt_m = 0               # 열에 경비가 없을때 카운트 

for i in range(n):
    if 'X'not in castle[i]:     # 행에 경비가 아에 없을 경우 cnt +1
        cnt_n += 1
for j in range(m):              
    if 'X' not in [castle[i][j] for i in range(n)]: # [j]값이 고정인 상태로 [i]값이 반복되도록 하여 열에 경비가 없는지 확인
        cnt_m += 1         

print(max(cnt_n,cnt_m)) # 행 또는 열에 빈곳을 채우기 위해 두 카운트 숫자 중 큰 값을 출력해야 다 채울 수 있음 