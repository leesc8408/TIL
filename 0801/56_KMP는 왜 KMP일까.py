# https://www.acmicpc.net/problem/2902

n = input().split('-')
name = [n[i][0] for i in range(len(n))]
# for i in range(len(n)):
#     name.append(n[i][0])
print(''.join(name))