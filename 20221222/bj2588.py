# https://www.acmicpc.net/problem/2588  곱셈

def num(a,b):
    answer = []
    for i in reversed(b):
        answer.append(int(a) * int(i))
    answer.append(int(a) * int(b))
    return answer

a = input()
b = input()

for _ in num(a, b):
    print(_)

# test_ = num(b)

# answer = int(a) * int(b)

# print(int(a) * int(test_[2]))
# print(int(a) * int(test_[1]))
# print(int(a) * int(test_[0]))
# print(answer)    


# a = input()
# b = input()
# for i in reversed(b):
#     print(int(a)*int(i))
# print(int(a)*int(b))