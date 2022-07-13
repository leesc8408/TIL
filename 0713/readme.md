# 🚩함수

> 편해지고 간결해지고 빠르고 재사용이 용이 하다
>
> 복잡한 내용을 숨기고, 기능에 집중하여 사용(블랙박스)



- 특정 기능을 하는 코드의 조각, 매번 다시 작성하지 않고 필요시에만 호출하여 편하게 사용



1. 사용자 함수
   - 구현되어 있는 함수가 없어 사용자가 직접 작성한 함수

2. 내장 함수
   - 파이썬 인터프리터에  항시 사용할 수 있도록 내장되어 있는 함수
3. pstdev 함수(파이썬표준 라이브러리 - statistics)
   - 내장 함수보다 더 편하게 사용할 수 있도록 파이썬 표준 라이브러리의 함수

---

### 선언과 호출

- 함수의 선언은 def 키워드를 사용

- 들여쓰기를 통해 function body(실행될 코드 블럭)을 작성함
- 함수는 매개 변수를 넘겨줄 수 있음
- 동작 후 return을 통해 결과를 반환하고 종료한다.

```python
# 정의	
# 1. def로 선언
# 2. 함수 이름 : add
# 3. Input : a, b
def add(a, b):
    # 4. return : 값을 반환
    return a + b

def minus(a, b):
    return a - b

# 호출
print(add(5, 10))	# 출력 = 15
print(minus(10, 5))	# 출력 = 5

# 내장 함수 호출
print(sum([1, 2, 3]))	# 모두 합하라. 출력 = 6
```

---

### 함수의 결과값 (output)

- 함수는 반드시 값을 하나만 return하고 종료된다.

  > 명시적인return이 없는 경우에도 None을 반환한다.

- 두 개 이상의 값을 반환하려면 **`튜플(tuple)`**로 반환한다.

- return은 함수의 값을 반환하는 `키워드`이고,

  print는 출력을 위해 사용되는 `함수`이다.

---

### 함수의 입력 (input)

- Parameter - 함수 내부에서 사용되는 식별자

- Argument - 함수를 호출할때, 넣어주는 값()

  ```python
  def cube(n):		# n = Parameter 
      return n ** 3
  print(cube(12))		# 12 = Argument 
  ```

1. Argument란?

   - 함수 호출 시 함수의 매개 변수를 통해 전달되는 값
   - 위치를 기본적으로 사용하며 키워드를 지정할 수도 있음

   ```python
   # 1. 위치적 
   def add(x, y):		# 함수내부로 전달은 순서에 따라 x가 2, y는 3을 받는다.
   	return x + y
   print(add(2, 3))	# Argument = 2, 3 의 순서
   #출력 = 5
   
   # 2. 키워드
   def add(x, y):
   	return x + y
   add(x=2, y=5)	# x=2,y=5로 x,y값을 지정 
   add(2, y=5)		# 위치,키워드 2가지 사용가능 (실행가능)
   add(x=2, 5)		# 키워드가 먼저 사용되면 위치는 사용불가 (실행불가) 
   ```

   - 변수 값을 설정하지 않아도 되도록 설정 가능

   ```python
   def add(x, y=0):	# y 값이 없을 수 있음을 표시
   	return x + y
   add(2)				# 입력값 2는 x에만 전달 y는 0이 된다
   ```

   - 정해지지 않은 개수의 값을 받는다

   ```python
   # 정해지지 않은 갯수의 인자
   def my_add(*numbers):
       # 내부적으로 numbers가 tuple
       return numbers 
   
   result = my_add(1, 2, 3)
   print(result, type(result)) # (1, 2, 3) <class 'tuple'>
   ```

   - 정해지지 않은 개수의 키워드 값을 받는다

   ```python
   def my_func(**kwargs):
       return kwargs
   
   result = my_func(name='홍길동', age='100', gender='M')
   print(result, type(result)) # {'name': '홍길동', 'age': '100', 'gender': 'M'} <class 'dict'>
   ```

---

### 함수의 범위 (scope)

- 함수는 코드 내부에 local scope를 생성하며, 그 외의 공간인 global scope로 구분
- 객체는 각자의 수명주기(lifecycle)가 존재
  - **built-in scope** : 파이썬이 실행된 이후부터 영원히 유지
  - **global scope** :모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유
  - **local scope** : 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

---

### 함수 응용

- **map**
  - 모든 반복 가능한 것에 내가 적용하고 싶은 하는 함수를 정한다

```python
# 반복문!
numbers = ['1', '2', '3']
print(numbers)
new_numbers = []
for number in numbers:
    new_numbers.append(int(number))
print(new_numbers)

# map!
numbers = ['1', '2', '3']
new_numbers_2 = map(int, numbers)
print(new_numbers_2, type(new_numbers_2)) # <map object at 0x0000023BE69A2C70> : 이미 함수가 모두 적용된 
print(list(new_numbers_2)) 
# 리스트로 형변환해서보면 바뀌어있다~!
# 보기 위해서 바꾼 것일 뿐! 반드시 list로 바꿔야하는 것은 아닙니다 :)
```

![img](https://cdn.discordapp.com/attachments/993047919076855868/996608655875121162/unknown.png)