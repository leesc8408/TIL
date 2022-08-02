# https://www.acmicpc.net/problem/23825
# n,m 입력 받아서 //2로 나눈 몫을 구해서 min값을 출력

n, m = map(int, input().split())
a = n//2    # S의 개수
b = m//2     # A의 개수
print(min(a,b)) # 