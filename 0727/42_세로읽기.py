# https://www.acmicpc.net/problem/10798

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/TIL/0727/_세로읽기.txt')

word_list = []
for _ in range(5):
    word_list.append(input())

for i in range(15):
    for j in range(5):
        try:
            print(word_list[j][i], end='')
        except:
            continue
