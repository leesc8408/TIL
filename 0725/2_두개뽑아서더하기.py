# https://school.programmers.co.kr/learn/courses/30/lessons/68644
def solution(numbers):
    answer = []
    hap_list = []

    for i in range(len(numbers)): 
        for i2 in range(i+1,len(numbers)):
            num1 = numbers[i]
            num2 = numbers[i2]
            hap = num1 + num2
            hap_list.append(hap)
    answer = sorted(set(hap_list))

    return answer


print(solution([2, 1, 3, 4, 1]))
print(solution([5, 0, 2, 7]))
