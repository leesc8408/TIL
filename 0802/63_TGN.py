# https://www.acmicpc.net/problem/5063

# 문제는 개그인듯 ㅡ.ㅡ;;;
# 첫째 줄에 테스트 케이스의 개수 N
# 다음 N개의 줄에는 3개의 정수 r, e, c
# r은 광고를 하지 않았을 때 수익
# e는 광고를 했을 때의 수익
# c는 광고 비용
# 광고를 해야 하면 "advertise", 하지 않아야 하면 "do not advertise", 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력
# r 과 e-c를 비교

import sys
sys.stdin = open('63_TGN.txt')

t = int(input())
for _ in range(t):
    r, e, c = map(int, input().split())
    if r < e-c:
        print('advertise')
    elif r == e-c:
        print('does not matter')
    else:
        print('do not advertise')