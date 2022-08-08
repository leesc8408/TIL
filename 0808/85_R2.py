# https://www.acmicpc.net/problem/3046

# s = (r1 + r2) // 2

r1, s = map(int, input().split())

r2 = (s * 2) - r1 
print(r2)