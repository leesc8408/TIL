from pprint import pprint
import sys
sys.stdin = open ('75_누울 자리를 찾아라.txt')

a = int(input())
room = [list(input()) for _ in range(a)]

h_cnt, v_cnt = 0, 0
h_len, v_len = 0, 0
for i in range(a):
    for j in range(a):
        #가로
        if room[i][j] == '.':
            h_len += 1
        else:
            h_len = 0
        print(h_len,end=' ')
        if h_len == 2:
            h_cnt += 1
        # 세로
        if room[j][i] == '.':
            v_len += 1
        else:
            v_len = 0
        if v_len == 2:
            v_cnt += 1

print(h_cnt, v_cnt)