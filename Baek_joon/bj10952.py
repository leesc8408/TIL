# https://www.acmicpc.net/problem/10952
    
while True:
    a, b = map(int, input().split())
    if (a, b) == (0, 0):
        break
    else:
        print(a + b)