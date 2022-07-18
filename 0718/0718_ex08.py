# 아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
# 코드에서 오류를 찾아 원인을 적고, 수정하세요.

# word = "HappyHacking"

# count = 0

# for char in word:
#     if char == "a" or "e" or "i" or "o" or "u": # char == 비교값 입력오류 (이러한 식으로 단축불가)
#         count += 1

# print(count)

word = "HappyHacking"

count = 0

for char in word:
    if char in "aeiou": # 수정
        count += 1

print(count)

# 또는

word = "HappyHacking"

count = 0

for char in word:
    if char == "a" or char =="e" or char =="i" or char =="o" or char =="u": # 각 비교값이 char에 적용되도록 수정
        count += 1

print(count)