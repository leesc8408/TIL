# https://school.programmers.co.kr/learn/courses/30/lessons/76501
# def solution(absolutes, signs):
answer = 0


absolutes = [1,2,3]
signs = [False,False,True]
p_li = [absolutes[i] for i in range(len(signs)) if signs[i] == True]
# p_li(True값 모음) =  signs의 길이 동안 반복하여 signs[i] 값이 True이면 absolutes[i]값을 추가
m_li = [absolutes[i] for i in range(len(signs)) if signs[i] == False]
# m_li(False값 모음) = 위와 동일하나 False이면 absolutes[i]값을 추가
answer = sum(p_li) - sum(m_li)
# 각 리스트를 합하고 꼭!! True값에서 False값을 뺀다  
print(answer)