import sys

sys.stdin = open("_괄호짝짓기.txt")

t = 10
for test_case in range(1, t + 1):
    n = int(input())
    n_list = list(input())

    list_1 = []
    # list_2 = []
    # list_3 = []
    # list_4 = []
# 처음 접근은 입력 리스트에서 한 자씩 빼서 각 기호별로 열린 기호이면 해당 기호 리스트에 append 닫힌 기호이면 pop
# 리스트에서 나온 하나의 기호를 기준으로 같은 식의 코드 4번 반복하며 진행 해서 각 리스트에 남은 기호가 있으면 0 없으면 1
# 헌데 만들고 보니 기호별로 리스트를 만들어 짝을 찾아 내는게 2차원 리스트인거 같아서 기호 리스트를 추가해서 
# 2차원 리스트의 탐색처럼 만듬. 
    giho = list('()[]<>{}')
    # print(giho)

    for j in range(0, len(giho), 2):
        for i in n_list:
            if i == giho[j]:
                list_1.append(i)
            elif i == giho[j + 1]:
                if giho[j] not in list_1:
                    list_1.append(i)
                else:
                    list_1.pop()
    if list_1:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')

# 주석을 달면서 생각된건데 입력 값인 기호 리스트는 
# 기호=[
#   [()(()))()())()))((()))]
#   [[[]][[[][[[[[[]]]]]]]
#   [{}{{{{{{}{}{{}}}}}}}]
#   [<><<<<<<><><>>><><]
#]
# 이런 2차원 리스트 중 리스트 안에 리스트로 값들을 모으지 않고 리스트 안에 무작위로 모아둔 상태로 
# 정리 하지 않은 2차원리스트 같다고 느겼음.

        # 노가다의 잔재들^^
        # if i == '[':
        #     list_2.append(i)
        # elif i == ']':
        #     if '[' not in list_2:
        #         list_2.append(i)
        #     else:
        #         list_2.pop()

        # if i == '{':
        #     list_3.append(i)
        # elif i == '}':
        #     if '{' not in list_3:
        #         list_3.append(i)
        #     else:
        #         list_3.pop()

        # if i == '<':
        #     list_4.append(i)
        # elif i == '>':
        #     if '<' not in list_4:
        #         list_4.append(i)
        #     else:
        #         list_4.pop()
                
    # if list_1 or list_2 or list_3 or list_4:
    #     print(f'#{test_case} 0')
    # else:
    #     print(f'#{test_case} 1')
