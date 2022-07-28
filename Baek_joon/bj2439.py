n = int(input())

for i in range(n):
    star = '*' * (i + 1)
    gong = ' ' * (n - len(star))
    print(f'{gong}{star}')