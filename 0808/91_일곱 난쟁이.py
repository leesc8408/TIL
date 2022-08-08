# https://www.acmicpc.net/problem/2309

import sys
sys.stdin = open('_일곱 난쟁이.txt')

t = 9
hobit = [int(input()) for _ in range(t)]
# print(hobit)
tall = 0

for i in range(t - 7):
    for j in range(1, t):
        
