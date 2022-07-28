# https://www.acmicpc.net/problem/2753
# (4의 배수임 and 100의 배수아님) or 400의 배수 = 1

a = int(input())
if a % 4 == 0 and a % 100 != 0:
    print(1)
elif a % 400 == 0:
    print(1)
else:
    print(0)