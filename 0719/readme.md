# 🚩OOP ( Object Oriented Programing)

- #### 객체 지향 프로그래밍 (OOP)

  - 컴퓨터 프로그래밍을 명령어의 목록으로 보는 시각에서 벗어나 여러 개의 독립된 단위

    객체들의 모임으로 파악하고자 하는 것

  - 장점
    - 프로그램을 유연하고 변경이 용이 하게 만들기 때문에 대규모 소프트웨어 개발에 많이 사용
    - 프로그래밍을 더 배우기 쉽게 하고 소프트웨어 개발과 보수를 간편하게 하며 보다 직관적인 코드 분석을 가능하게 하는 장점을 가짐

---

- 객체(object)

  > 객체(object)는 특정 타입(type)의 인스턴스(instance)이다

  - 클래스에서 정의한 것을 토대로 메모리(**`실제 저장공간`**)에 할당된 것

  - 타입(class)과 값(instance)

  - 객체의 특징

    - 타입(type) : 어떤 연산자와 조작이 가능 한가?

    - 속성(attribute) : 어떤 상태를 가지는가?

    - 조작법(method) : 어떤 해위를 할 수 있는가? 

객체 지향 이전에는 절차 지향 프로그래밍이 일반적으로 사용됨

예시

```python
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def circumference(self):
        return 2 * (self.x + self.y)

r1 = Rectangle(10, 30)
r1.area()
r1.circumference()

r2 = Rectangle(300, 20)
r2.area()
r2.circumference()
```

- 사각형(Rectangle) - 클래스
- 두개의 사각형(r1, r2) - 인스턴스
- 사각형의 정보(가로,세로) - 속성
- 사각형의 행동/기능(넓이,높이) - 메소드



직관적인 예시

```python
my_list = [1, 3, 2]
# 리스트의 데이터를 직접 정렬
my_list.sort()
print(my_list)	# [1, 2, 3] 리스트가 주체로써 변경되었기에 바로 사용가능

my_list = [5, 4, 6]
# 리스트는 sorted 함수의 값으로 전달(사용)될 뿐
sorted(my_list)
print(my_list)	# [5, 4, 6] 리스트에 sorted 함수가 빠지면 기능이 없어짐
```

---

## OOP 기초

- 기본 문법

  ```python
  # 클래스 정의
  class MyClass: # class의 이름은 CamelCase로 지정한다(대.소문자)
    pass
  
  # instance 생성
  my_instance = MyClass() # instance의 이름은 snake_case로 지정한다(_를 사용)
  # method 호출
  my_instance.my_method()
  # attribute
  my_instance.my_attribute
  ```

  - 속성 : 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
  - 메소드 : 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)



- 객체 비교하기

  - ==
    - 동등한(메모리 주소는 다름)
    - 두 변수가 가진 값이 같을 경우 참
  - is
    - 동일한(메모리 주소가 같음)
    - 각 변수가 동일한 값일 경우 참

  예시

  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  # 두 변수가 값(list)이 같으므로 == 는 참
  # 두 변수의 값은 같으나 저장되는 메모리 상으로는 각각 위치(메모리a,메모리b)가 다른 상태라 is 는 거짓
  
  a = [1, 2, 3]
  b = a
  # 두 변수가 값(list)이 같으므로 == 는 참
  # 두 변수의 값이 저장되는 메모리는 같은 위치(메모리a) 상태라 is 는 참
  ```


---

- 인스턴스 변수
  - 인스턴스가 개인적으로 가지고 있는 속성(attribute)
  - 각 인스턴스들의 고유한 변수


```python
class Person:
  	def __init__(self, name, age, gender): # name, age 등이 인스턴스
      	self.name = name	# name 인스턴스 변수 정의
        self.age = age
        self.gender = gender

    def info(self):
      	return (self.name, self.age, self.gender)

hong = Person('홍길동', 100, 'M')	# name 인스턴스 변수 할당
ko = Person('고길동', 40, 'M')

print(hong.info())
print(hong.name)	# name 인스턴스 변수 접근
print(hong.age)
```

- 인스턴스 메소드

  - 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
  - 호출시, 첫번째 인자로 인스턴스 자신(self)이 전달됨

- self

  - 인스턴스 자신
  - 호출 시 ()에 첫번째로 입력되어 자신이 전달되도록 함
  - 파이썬의 암묵적 규칙

- 생성자(Constructor) 메소드

  - 인스턴스 객체가 샌성될 때 자동으로 호출되는 메소드

  ```python
  class Person:
      
      def __init__(self, name):
          print(f'인스턴스가 생성되었습니다. {name}')
          
  personl = Person('지민')
  # 인스턴스가 생성되었습니다. 지민
  ```

  

- 소멸자(destructor) 메소드

  - 인스턴스 객체가 소멸되기 직전에 호출되는 메소드

  ```python
  class Person:
      
      def __del__(self):
          print(f'인스턴스가 사라졌습니다.')
          
  personl = Person()
  del personl
  # 인스턴스가 사라졌습니다
  ```

  
