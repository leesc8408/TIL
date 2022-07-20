a, b = map(int, input().split())
-2147483648 <= a, b <= +2147483647

y = a if (a >= b) else b
print(y)