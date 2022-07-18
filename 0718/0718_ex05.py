# 아래 코드는 숫자의 길이를 구하는 코드입니다.
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# number = 22020718
# print(len(number))

# 에러 메세지
# TypeError: object of type 'int' has no len()

# 원인
# len함수에 입력값에는 int타입을 사용할 수 없다는 에러.

number = '22020718' # ''입력으로 str치환
print(len(number))

# 또는 

number = 22020718
print(len(str(number))) # 출력문에서 str() 추가하여 str치환 후 출력
