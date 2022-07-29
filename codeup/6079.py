n = int(input())
cnt = 0
for i in range(n):
    cnt += i
    if cnt >= n:
        print(i)
        break