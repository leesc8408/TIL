import sys

sys.stdin = open("34_슈퍼 마리오.txt")

# score_list = []
# score = 0

# for i in range(10):
#     score_list.append(int(input()))

# for i in score_list:
#     score += i
#     if score >= 100:
#         if score - 100 > 100 - (score - i):
#             score -= i
#         break      
# print(score)    


score_list = []
score = 0

for i in range(10):
    score_list.append(int(input()))

for i in score_list:
    score += i
    if score >= 100:
        prev_score = score - i 
        out = prev_score if score - 100 >= 100 - prev_score else score
        break
    else:
        out = score
print(out) 
