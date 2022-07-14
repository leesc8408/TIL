# 문자열 word가 주어질 때, Dictionary를 활용해서 해당 문자열에서 
# 등장한 모든 알파벳 개수를 구해서 출력하세요.

# 문제 18.  알파벳 등장 갯수 구하기

word = 'banana'
dic = {}

# for char in word:
#     if not char in dic:
#         dic[char] = 1
#     else:
#         dic[char] = dic[char] + 1
# print(dic)


for char in word:
    dic[char] = dic.get(char, 0) + 1
print(dic)

# 출력
for key in dic:
    print(key, dic[key])
