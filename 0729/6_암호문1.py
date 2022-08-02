from posixpath import split
import sys

sys.stdin = open("_암호문1.txt")

for test_case in range(1, 11):
    amho_len = int(input())
    amho = input().split()
    mi_len = int(input())
    mi_list = input().split()

    for i in range(len(mi_list)):
        if mi_list[i] == 'I':
            x = int(mi_list[i+1])
            y = int(mi_list[i+2])
            s_list = mi_list[i+3 : i+3+y]
            for j in mi_len:
                for h in s_list:
                    
