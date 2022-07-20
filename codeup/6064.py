a, b, c = map(int, input().split())
-2147483648 <= a, b,c <= +2147483647

x = a if a<b else b
y = x if x<c else c
print(y)
