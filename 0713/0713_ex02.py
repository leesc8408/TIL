# print('가로 세로 값을 입력하세요.')

# a, b = map(int, input().split())
# # print(a, b, type(a), type(b))

def rectangle(a, b):
    return a * b, (a + b) * 2

print(rectangle(20 , 30)) 


# 업그레이드

# a, b = map(int, input().split())

# if a or b <= 0:
#     print('0이상의 정수를 입력하세요')
# else:
#     def rectangle(a, b):
#         return a * b, (a + b) * 2

#     print(rectangle(a , b)) 