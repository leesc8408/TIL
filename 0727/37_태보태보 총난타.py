# https://www.acmicpc.net/problem/17249

t = input()
l_punch = 0
r_punch = 0
cnt = 0

for i in t:
    if i == '@':
        cnt +=1
    elif i == '(':
        l_punch = cnt
        cnt = 0
r_punch = cnt
print(l_punch, r_punch)    