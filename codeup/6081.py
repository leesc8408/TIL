n = input().upper()

n10 = int(n, 16)
for i in range(1,16):
    out = n10 * i
    i16 = format(i, 'X')
    out16 = format(out, 'X')
    print(f'{n}*{i16}={out16}')