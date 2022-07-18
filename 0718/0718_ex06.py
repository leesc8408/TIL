# 아래 코드는 1부터 N까지의 숫자에 2를 곱해서 변수에 저장하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# N = 10
# answer = ()
# for number in range(N + 1):
#     answer.append(number * 2)

# print(answer)

# 에러 메세지
# AttributeError: 'tuple' object has no attribute 'append'

# 원인
# tuple객체는 값을 append 할수 없어 발생한 오류.

N = 10
answer = []     # list로 치환
for number in range(N + 1):
    answer.append(number * 2)

print(answer)