# 🚩제어문

- 파이썬의 기본적으로 위에서 아래로 오른쪽에서 왼쪽으로 명령을 수행하는데

  특정 상황에 따라 선택적 실행 / 반복적 실행하도록 하는 것을 말한다

- 제어문은 순서도로 표현 가능하며 `조건문`과 `반복문`이 있다

---

### - 조건문

- 조건문은 참 / 거짓을 판단할 수 있는 조건식과 함께 사용

  - 기본 형식 

    ```py
    if <expression>:  
        # run code <- 참 일 경우 실행
    else:
        # run code <- 거짓 일 경우 실행
    ```

  - 예시

    ```py
    a = -10
    if a >= 0:   # a는 0 이상이다 참이면 바로 코드 실행 거짓이면 else: 코드 실행
        print('양수')  # 참 일 경우 실행
    else:
        print('음수')  # 거짓 일 경우 실행
    print(a)
    '음수'
    -10
    ```

  - 조건 표현식 - print에 잘 사용하진 않으나 사용 할 수 있으니 알아두자

    ![img](https://cdn.discordapp.com/attachments/995988625160405102/996226076307107850/unknown.png)

---

### - 반복문

- 특정 조건에 도달할 때까지 반복하는 문장

1. while 문

   - expression이 참인 경우 계속 실행

   - 종료를 위해 expression에 종료 조건을 넣어서 무한루프 방지

     ```py
     # 기본형식
     while <expression>:
     	# code block
     
     
     # 예시
     
     a = 0
     while a < 5:    # 1. a가 5보다 작으면 참 들여쓰기 되어있는 줄 실행
     	print(a)    # 2. a를 반환(출력)한다
     	a += 1      # 3. a에 1을 더한다 참이 었으므로 1.부터 반복 실행
     print('end')    # 4. a가 5보다 작아져서 거짓이 되었다면 end를 출력한다
     ```

---

2. for 문

   - 시퀀스를 포함한 순회 가능한 객체 요소를 순회한다

   - 처음부터 끝까지 순회 하기때문에 별도의 종료 조건은 필요없음

     ```py
     # 기본 형식
     for <변수명> in <반복 가능한 아이(iterable)>:
         # Code block
     
     
     # 예시
     
     for fruit in ['apple', 'mango', 'banana']: 
         print(fruit)  # 첫번째 str인 'apple'을 시작으로 1개씩 순서대로 print 한다 
     print('끝')
     
     # 출력 
     apple
     mango 
     banana
     끝
     ```

   - 문자열 순회

     - 사용자가 입력한 문자(str)를 한 글자씩 세로 출력한다

     - 사용자가 입력한 문자(str)를 range 사용하여 세로 출력한다.

       index를 기준하여 순회해서 장점이 있음.  알고리즘 활용에서 많이 사용. 

     ```py
     # 기본 문자열 순회
     chars = input()  # hi 입력
     
     for char in chars:
         print(char)
     
     # 출력
     h
     i
     
     # range 사용 문자열 순회
     chars = input()  # hi 출력
     
     for idx in range(len(chars)):   # range(len(chars)) 활용
         print(chars[idx])   # index를 기준해서 chars(문자열)의 0부터 순서대로 출력된다
     						# 기본과 다르게 index 때문에 특정부분출력, 역순 등 활용가능.
     # 출력
     h
     i
     ```

   - enumerate 순회 - 잘 안씀

   - 딕셔너리 순회

     - 기본적으로 key를 순회하고 key를 통해 값을 사용 한다

     ```py
     # 예시
     grades = {'john': 80, 'eric': 90}
     for name in grades:
         print(name)
     
     # 출력    
     john
     eric      
     
     
     # 출력 된 key값을 사용
     
     grades = {'john': 80, 'eric': 90}
     for name in grades:
         print(name, grades[name])
     
     # 출력
     john 80
     eric 90    
     ```

---

### - 반복문의 제어

- break

  - 반복 실행중 만나면 종료됨

    ```py
    # 예시
    n = 0
    while True:    # 참 다음 실행
        if n == 3:    # n이 3과 같다 참이면 들여쓰기 코드 실행 
              break
        print(n)   # if n == 3 이 거짓이면 실행
        n += 1   
    
    # 출력
    0
    1
    2
    ```

- continue

  - continue 이후의 코드블럭을 수행하지 않고 다음 반복을 실행

    ```py
    # 예시
    for i in range(6):   # 1. range로 0~5까지 i에 순서대로 출력
        if i % 2 == 0:   # 2. i가 짝수이면 continue 실행
            continue   # 3. 실행 되면 아래 코드 실행없이 1번으로 건너뜀
        print(i)
        
    ```

    

- for-else

  - for 문장에서 break가 실행되면 else를 출력

    break가 실행되지 않으면 줄력 안 함.

    ```py
    # 예시
    for char in 'apple':
        if char == 'b':   # char문자열에 b가 있나? 없으면 반복
            print('b!')   
            break    # 조건이 없어 break가 사용 안됨
    else:    # 마지막으로 else 실행
        print('b가 없습니다')
    
    # 출력
    b가 없습니다.
    
    
    # 예시
    for char in 'banana':
        if char == 'b':   # char문자열에 b가 있나? 있으면 들여쓰기 실행
            print('b!')   # 'b'가 있으므로 출력실행 후 다음
            break         # break 반복 중단!!
    else:
        print('b가 없습니다')
    
    # 출력
    b!
    ```

    