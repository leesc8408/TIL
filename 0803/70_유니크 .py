# https://www.acmicpc.net/problem/5533

# 1 <= x <= 100  동일한 수가 없다면 점수, 있으면 점수 없음  진행횟수 3번
# 1줄 n = 행 = 참가자수 / 2줄부터 n개줄에 각 플레이어 제출 점수 3개(열) 공백 구분 입력
# 3번 게임 진행 후 획득 점수

from pprint import pprint
import sys
sys.stdin = open('70_유니크 .txt')

t = int(input())
score_ = [list(map(int, input().split())) for _ in range(t)]
score = 0

for i in range(t):
    for j in range(3):
        card = score_[j]
        if card != [score_[i][j] for i in range(1, t)]:
            score += card
    # print(score)
        
