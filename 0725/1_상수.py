# https://www.acmicpc.net/problem/2908
from audioop import reverse
from pickletools import read_bytes4, read_bytes8
import sys

sys.stdin = open("1_상수.txt")
#입력
a, b = map(int, input().split())

#연산
#입력값 역순 변환
a_list = reversed(list(str(a))) # int -> str -> list로 2번에 걸쳐 변환 후 리버스
b_list = reversed(list(str(b)))
c = int(''.join(a_list))    # 리버스된 리스트 값을 join으로 str로 변환 후 int로 다시 변환 
d = int(''.join(b_list))

#변환값 비교 출력
if c < d:
    print(d)
else:
    print(c)
