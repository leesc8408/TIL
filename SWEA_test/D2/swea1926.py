from hashlib import new
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
n_list = map(str, (list(range(1, T+1))))
# print(n_list, type(n_list))
for i in n_list:
    # print(i, end=' ')
    if i in '3':
        new_i = i.replace('3','-')
    print(new_i, end=' ')
    # if new_i 
