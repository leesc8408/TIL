# https://school.programmers.co.kr/learn/courses/30/lessons/81301

# 숫자중 일부 영단어 수정 입력
# 입력값을 모두 숫자로 변환


# s = input()
# s_dic = {
#     'zero' : '0',
#     'one' : '1',
#     'two' : '2',
#     'three' : '3',
#     'four' : '4',
#     'five' : '5',
#     'six' : '6',
#     'seven' : '7',
#     'eight' : '8',
#     'nine' : '9'
# }

# for k, v in s_dic.items():
#     if k in s:
#         s = s.replace(k, v)
# print(s)

def solution(s):

    s_dic = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9'
    }

    for k, v in s_dic.items():
        if k in s:
            s = s.replace(k, v)    
    return int(s)

print(solution('123'))