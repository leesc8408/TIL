# https://www.acmicpc.net/problem/1269

# 집합 a  집합b 있고 두 집합의 대칭 차집합의 원소개수를 출력
# a-b와 b-a의 합집합이 a,b의 대칭 차집합(^)이다

# A = { 1, 2, 4 }, B = { 2, 3, 4, 5, 6 }
# 일때
# A-B = { 1 }, B-A = { 3, 5, 6 } 
# 이므로  대칭 차집합의 원소의 개수는 1 + 3 = 4개

import sys
sys.stdin = open('61_대칭 차집합.txt')

a, b = map(int, input().split())        # 3 5
a_list = set(map(int, input().split())) # {1, 2, 4}
b_list = set(map(int, input().split())) # {2, 3, 4, 5, 6}
c_list = a_list ^ b_list                # {1, 3, 5, 6}

print(len(c_list))                      # len으로 개수만 출력