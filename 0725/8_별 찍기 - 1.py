# https://www.acmicpc.net/problem/2438

n = int(input())
for i in range(n):
    out = '*' * (i + 1) # 인덱스 i가 증가로 별이 늘어남
    print(out)