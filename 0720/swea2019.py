# 2019. 더블더블 
# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
out = 1

for i in range(0, T + 1):
    print(out, end=' ')
    if i != T + 2:
        out = out*2