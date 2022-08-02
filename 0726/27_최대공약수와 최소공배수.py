# https://www.acmicpc.net/problem/2609
import sys

sys.stdin = open("27_최대공약수와 최소공배수.txt")
#입력
a,b = map(int, input().split())
#연산
a_list = [i for i in range(1, a+1) if a % i == 0]   # a의 약수 리스트
b_list = [i for i in range(1, b+1) if b % i == 0]   # b의 약수 리스트
yak = 0

for i in a_list:
    for i2 in b_list:
        if i == i2:     # 각 리스트에서 같은 값을 찾아서 약수(yak)에 할당
            yak = i     # 리스트가 오름차순이므로 마지막 할당 값은 최대공약수
bea = a * b // yak      # 최소공배수 = 두 수의 곱을 최대공약수로 나눈 값
#출력
print(yak, bea, sep='\n')



