# https://www.acmicpc.net/problem/2495

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/01-ALGORITHM/1회차/이순철/20220811/_연속구간.txt')

for _ in range(3):
    num = input()
    cnt = 1
    nu = 0
    for i in range(len(num) - 1):
        if num[i] == num[i + 1]:
            cnt += 1
        else:
            if cnt > nu:
                nu = cnt
            cnt = 1
        # print(cnt, nu)
    if nu >= cnt:
        print(nu)
    else:
        print(cnt)