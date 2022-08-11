# https://www.acmicpc.net/problem/2857

import sys
sys.stdin = open('/Users/lsc08/OneDrive/바탕 화면/01-ALGORITHM/1회차/이순철/20220811/_FBI.txt')

FBI = []
for i in range(1,6):
    code_name = input()
    if 'FBI' in code_name:
        FBI.append(i)
if FBI:
    print(*FBI, sep=' ')
else:    
    print('HE GOT AWAY!')