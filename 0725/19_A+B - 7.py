# https://www.acmicpc.net/problem/11021

t = int(input())
for test_csae in range(1, t + 1):
    a, b = map(int, input().split())
    print(f'Case #{test_csae}: {a + b}')