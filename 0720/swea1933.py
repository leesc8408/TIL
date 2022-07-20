# 1933. 간단한 N 의 약수
# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for i in range(1, T+1):
    if T %i ==0:
        print(i, end=' ')