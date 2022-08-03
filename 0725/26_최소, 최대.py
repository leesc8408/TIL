# https://www.acmicpc.net/problem/10818

t = int(input())
t_list = list(map(int, input().split()))

n = min(t_list)
m = max(t_list)
print(n, m)