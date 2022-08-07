# https://www.acmicpc.net/problem/2789

word = input().upper()

for i in 'CAMBRIDGE':
    word = word.replace(i, '')
print(word)
