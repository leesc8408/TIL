
import sys

sys.stdin = open("33_크로아티아 알파벳.txt")


cro = input()
# print(cro)
cro_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']   # 크로아티아 알파벳의 리스트
for i in cro_a:                 # 크로아티아 알파벳을 한 개씩 꺼내어
    cro = cro.replace(i, '*')   # 입력값cro에서 찾아 '*'로 변환하고 다시 cro에 할당
    # print(cro)                # 위를 반복하며 cro값에 있는 크로아티아 알파벳을 모두 '*'변환
print(len(cro))                 # 변환된 *과 나머지 문자의 길이를 출력

# cro값의 변환 과정
# ljes=njak
# ljes=njak
# ljes=njak
# ljes=njak
# *es=njak
# *es=*ak
# *e**ak
# *e**ak  <- 최종적으로는 *이 3개, 알파벳 3개로 문자열의 길이는 6이 됨