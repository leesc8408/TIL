def rev(a):
    a = reversed(a)
    a = ''.join(a)

    return a
import sys
sys.stdin = open('84_단어 뒤집기.txt')

t = int(input())
for i in range(t):
    word = list(input().split())
    for a in word:
        print(rev(a), end=' ')
    print()
