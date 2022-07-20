import sys
sys.stdin = open("input.txt", "r")

n = int(input())
a = list(map(int, input().split()))

a.sort()
# print(a)
print(a[n//2])


    
