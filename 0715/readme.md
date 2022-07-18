# 🚩파이썬 표준 라이브러리

- 파이썬에서 기본적으로 설치된 모듈과 내장 함수의 모음

---

## - 모듈

- 편리한 함수를 각 프로그램에 정의를 복사하지 않고,

  사용할 수 있도록 정의를 파일에 넣어서 사용하는 방법

#### - 사용 예시

```python
import datetime

now = datetime.datetime.now()
print(now, type(now))

# 2022-07-18 22:32:11.855348 <class 'datetime.datetime'>
```

```python
import random

numbers = random.sample(range(1, 46), 6)
numbers.sort()
print(numbers, type(numbers))

# [8, 11, 19, 32, 34, 42] <class 'list'>
```

---

## - 파일 읽고 쓰기

- Open (파일 열기)
  - 모드
    - `'r'` : read (읽기 전용), **기존 파일을 읽어옴**.
    - `'w'` : write (쓰기 전용 - 덮어씀), **새로 파일을 생성하여 기록함**.
    - `'a'` : append (쓰는데 파일 있으면 이어서 씀), **기존 파일에 이어서 기록함**.

```python
with open('test.txt', 'w', encoding='utf-8') as f:
	#open('경로/파일명', '모드', '인코딩')
    
    f.write('Happy Hacking!\n')
    for i in range(1, 6):
        f.write(f'{i} 번째!\n')
```

---

## - json 사용

- 문자열로 이루어진 형식의 포맷

```python
import json 
from pprint import pprint

	# 파일을 열고, 
f = open('stocks.json', 'r', encoding='utf-8')
# JSON을 파이썬 객체(kospi) 형식으로 한다!
kospi = json.load(f)
samsung = kospi['stocks'][0]
# print(samsung, type(samsung))

# stockName 정보랑, closePrice 정보만 가진 딕셔너리를 만들고 싶어요!
result = {
    'stockName': samsung.get('stockName'),
    'closePrice': samsung.get('closePrice')
}

print(result)
```

