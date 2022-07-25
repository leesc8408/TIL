import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a1, b1, a2, b2 = map(int, input().split())
    1 <= a1, b1 <= 12
    0 <= b1, b2 <= 59
    h = 0
    m = 0

    m = b1 + b2
    if m > 59:
        h += 1
        m -= 60

    h = a1 + a2 + h
    if h > 12:
        h -= 12 

    print(f'#{test_case} {h} {m}')
