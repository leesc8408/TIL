# https://www.acmicpc.net/problem/7785

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/TIL/0728/_회사에 있는 사람.txt')

n = int(input())
person = [input().split() for _ in range(n)]
out = []
for i in range(n):
    if person[i][1] == 'enter':
        out.append(person[i][0])
    elif person[i][1] == 'leave':
        out.remove(person[i][0])
out = sorted(out, reverse=True)
print(*out, sep='\n')