# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

t = int(input())
for test_case in range(1, t + 1):
    ox = input()
    cnt = 0
    nu = 1
    for i in range(len(ox)):
        if ox[i] == 'O':
            if ox[i-1] == 'O' and i != 0:
                nu += 1
            else:
                nu = 1
            cnt += nu
    print(cnt)
