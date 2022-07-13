def gugu(n):
    print(n, '단', sep='')
    for i in range(1, 9 + 1):
        print(f'{n} X {i} = {n * i}')

for i in range(2, 9 + 1):
    gugu(i)