# 두 수를 Input으로 받아 합을 구하는 코드이다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# input = 10 20
# numbers = input().split()
# print(sum(numbers))

# 에러 메세지
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# 원인
# sum 함수에서 지원하지 않는 타입에 의한 에러.

numbers = map(int, (input().split()))   # map(int, )  추가하여 int치환
print(sum(numbers))