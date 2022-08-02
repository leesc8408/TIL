# https://www.acmicpc.net/problem/1292
# 122333444455555 문자수열에서 인덱스 a 부터 b 에 해당하는 숫자의 합
ln, hn = map(int, input().split())
list1 = []

for i in range(1, hn + 1): 
    for i2 in range(i):
        list1.append(i)
hap = 0
for i3 in range(ln - 1, hn):
    hap += list1[i3]
print(hap)