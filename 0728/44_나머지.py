# https://www.acmicpc.net/problem/3052
import sys

sys.stdin = open("44_나머지.txt")

# 입력값 % 42 를 10번 반복해서 리스트에 담아 set으로 중복 없애고 len으로 갯수를 출력

list1 = []
for i in range(10):
    list1.append(int(input()))
list2 = []
for i2 in list1:
    list2.append(i2 % 42)
print(len(set(list2)))