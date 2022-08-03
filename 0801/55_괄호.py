# https://www.acmicpc.net/problem/9012
import sys
sys.stdin = open('55_괄호.txt')

for _ in range(int(input())):
    n = input()
    vps = []

    for i in n:
        if i == '(':
            vps.append(i)
        elif i == ')':
            if '(' not in vps:
                vps.append(')')
            else:    
                vps.pop()
        
    print('YES' if len(vps) == 0  else 'NO')