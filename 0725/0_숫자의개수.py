# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
#입력
a = int(input())    
b = int(input())
c = int(input())

#연산
total = a * b * c
num_list = [0] * 10 # 0~9 까지 카운팅 할 리스트 
for i in str(total):    # 합계값을 str로 변환하여 한자리씩 반복문
    num_list[int(i)] += 1   # i값을 int로 변환하여 num_list[i] 인덱스 자리에 + 1 반복

#출력
for out in num_list:    # 완료된 num_list를 출력양식에 맞게 반복 출력
    print(out)


