n = int(input())
# print(n)
num = []

for i in range(1, n + 1):
    # print(i)
    if i %2 == 0:
        num.append(i)
print(sum(num))
