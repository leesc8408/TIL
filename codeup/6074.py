n = ord(input())
# print(n)
a = ord('a')
cnt = n - a

for i in range(cnt + 1):
    # print(i)
    out = a + i
    print(chr(out), end=' ')