# https://www.acmicpc.net/problem/2480

a, b, c = map(int, input().split())
out = 0

if a == b and b == c:
    out = 10000+a*1000
elif a == b or a == c:
    out = 1000+a*100
elif b == c:
    out = 1000+b*100
else:
    out = max(a,b,c)*100

print(out)