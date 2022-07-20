a, b = map(int, input().split())
c = bool(a)
d = bool(b)
print(not(c or d) >= ((not c) and (not d)))