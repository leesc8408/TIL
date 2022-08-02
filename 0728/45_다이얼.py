# https://www.acmicpc.net/problem/5622
char_dict = {
    'abc' : '3', 
    'def' : '4', 
    'ghi' : '5', 
    'jkl' : '6', 
    'mno' : '7', 
    'pqrs' : '8', 
    'tuv' : '9', 
    'wxyz' : '10'
    }
n = input().lower() # 소문자로 변환
sec_list = []   # 버튼당 초수 모음

for a in n:     
    for b in char_dict.keys():
        if a in b:
            sec_list.append(char_dict[b])
print(sum(map(int, (sec_list))))
