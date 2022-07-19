# 정수 number가 주어질 때, 각 자릿수의 합을 구해서 출력하세요. 

num = int(input())
ans = 0

while num != 0:
    ans += num%10
    num = num//10

print(ans)