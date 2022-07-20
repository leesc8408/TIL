a, b, c = map(int, input().split())
-2147483648 <= a, b,c <= +2147483647

num = [a, b, c]
for i in num:
    if i %2 == 0:
        print(i)
