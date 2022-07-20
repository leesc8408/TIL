a =int(input())
-2147483648 <= a <= +2147483647
a != 0

if a < 0:
    if a %2 == 0:
        print('A')
    else:
        print('B')
else:
    if a %2 == 0:
        print('C')
    else:
        print('D')
