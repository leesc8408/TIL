# 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# input = I'm Tutor 6

# words = list(map(int, input().split()))
# print(words)

# 에러 메세지
# ValueError: invalid literal for int() with base 10: "I'm"

# 원인
# 입력값인 value에 int가 아닌 타입의 입력으로 인한 에러.

words = list(input().split())   # map(int, ) 를 삭제하여 str치환
print(words)
