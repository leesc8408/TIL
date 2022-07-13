# 5의 개수 세기
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]

cnt = 0
for a in numbers:
    if a == 5:
        cnt += 1
print(cnt)

# upgrade

print(numbers.count(17))
