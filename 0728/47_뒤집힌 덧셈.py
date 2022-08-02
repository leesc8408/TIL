# https://www.acmicpc.net/problem/1357
def rev(a):
    a = reversed(a)
    a = ''.join(a)

    return int(a)

x, y = input().split()
out = rev(x) + rev(y)
print(rev(str(out)))