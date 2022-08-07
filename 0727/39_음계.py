# https://www.acmicpc.net/problem/2920

t = list(map(int, input().split()))
cnt = 0

for i in range(8):
    if t[i] == i + 1:
        cnt += 1
    elif t[i] == 8 - i:
        cnt -= 1
if cnt == 8:
    print('ascending')
elif cnt == -8:
    print('descending')
else:
    print('mixed ')