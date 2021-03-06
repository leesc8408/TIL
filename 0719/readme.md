# π©OOP ( Object Oriented Programing)

- #### κ°μ²΄ μ§ν₯ νλ‘κ·Έλλ° (OOP)

  - μ»΄ν¨ν° νλ‘κ·Έλλ°μ λͺλ Ήμ΄μ λͺ©λ‘μΌλ‘ λ³΄λ μκ°μμ λ²μ΄λ μ¬λ¬ κ°μ λλ¦½λ λ¨μ

    κ°μ²΄λ€μ λͺ¨μμΌλ‘ νμνκ³ μ νλ κ²

  - μ₯μ 
    - νλ‘κ·Έλ¨μ μ μ°νκ³  λ³κ²½μ΄ μ©μ΄ νκ² λ§λ€κΈ° λλ¬Έμ λκ·λͺ¨ μννΈμ¨μ΄ κ°λ°μ λ§μ΄ μ¬μ©
    - νλ‘κ·Έλλ°μ λ λ°°μ°κΈ° μ½κ² νκ³  μννΈμ¨μ΄ κ°λ°κ³Ό λ³΄μλ₯Ό κ°νΈνκ² νλ©° λ³΄λ€ μ§κ΄μ μΈ μ½λ λΆμμ κ°λ₯νκ² νλ μ₯μ μ κ°μ§

---

- κ°μ²΄(object)

  > κ°μ²΄(object)λ νΉμ  νμ(type)μ μΈμ€ν΄μ€(instance)μ΄λ€

  - ν΄λμ€μμ μ μν κ²μ ν λλ‘ λ©λͺ¨λ¦¬(**`μ€μ  μ μ₯κ³΅κ°`**)μ ν λΉλ κ²

  - νμ(class)κ³Ό κ°(instance)

  - κ°μ²΄μ νΉμ§

    - νμ(type) : μ΄λ€ μ°μ°μμ μ‘°μμ΄ κ°λ₯ νκ°?

    - μμ±(attribute) : μ΄λ€ μνλ₯Ό κ°μ§λκ°?

    - μ‘°μλ²(method) : μ΄λ€ ν΄μλ₯Ό ν  μ μλκ°? 

κ°μ²΄ μ§ν₯ μ΄μ μλ μ μ°¨ μ§ν₯ νλ‘κ·Έλλ°μ΄ μΌλ°μ μΌλ‘ μ¬μ©λ¨

μμ

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

- μ¬κ°ν(Rectangle) - ν΄λμ€
- λκ°μ μ¬κ°ν(r1, r2) - μΈμ€ν΄μ€
- μ¬κ°νμ μ λ³΄(κ°λ‘,μΈλ‘) - μμ±
- μ¬κ°νμ νλ/κΈ°λ₯(λμ΄,λμ΄) - λ©μλ



μ§κ΄μ μΈ μμ

```python
my_list = [1, 3, 2]
# λ¦¬μ€νΈμ λ°μ΄ν°λ₯Ό μ§μ  μ λ ¬
my_list.sort()
print(my_list)	# [1, 2, 3] λ¦¬μ€νΈκ° μ£Όμ²΄λ‘μ¨ λ³κ²½λμκΈ°μ λ°λ‘ μ¬μ©κ°λ₯

my_list = [5, 4, 6]
# λ¦¬μ€νΈλ sorted ν¨μμ κ°μΌλ‘ μ λ¬(μ¬μ©)λ  λΏ
sorted(my_list)
print(my_list)	# [5, 4, 6] λ¦¬μ€νΈμ sorted ν¨μκ° λΉ μ§λ©΄ κΈ°λ₯μ΄ μμ΄μ§
```

---

## OOP κΈ°μ΄

- κΈ°λ³Έ λ¬Έλ²

  ```python
  # ν΄λμ€ μ μ
  class MyClass: # classμ μ΄λ¦μ CamelCaseλ‘ μ§μ νλ€(λ.μλ¬Έμ)
    pass
  
  # instance μμ±
  my_instance = MyClass() # instanceμ μ΄λ¦μ snake_caseλ‘ μ§μ νλ€(_λ₯Ό μ¬μ©)
  # method νΈμΆ
  my_instance.my_method()
  # attribute
  my_instance.my_attribute
  ```

  - μμ± : νΉμ  λ°μ΄ν° νμ/ν΄λμ€μ κ°μ²΄λ€μ΄ κ°μ§κ² λ  μν/λ°μ΄ν°λ₯Ό μλ―Έ
  - λ©μλ : νΉμ  λ°μ΄ν° νμ/ν΄λμ€μ κ°μ²΄μ κ³΅ν΅μ μΌλ‘ μ μ© κ°λ₯ν νμ(ν¨μ)



- κ°μ²΄ λΉκ΅νκΈ°

  - ==
    - λλ±ν(λ©λͺ¨λ¦¬ μ£Όμλ λ€λ¦)
    - λ λ³μκ° κ°μ§ κ°μ΄ κ°μ κ²½μ° μ°Έ
  - is
    - λμΌν(λ©λͺ¨λ¦¬ μ£Όμκ° κ°μ)
    - κ° λ³μκ° λμΌν κ°μΌ κ²½μ° μ°Έ

  μμ

  ```python
  a = [1, 2, 3]
  b = [1, 2, 3]
  # λ λ³μκ° κ°(list)μ΄ κ°μΌλ―λ‘ == λ μ°Έ
  # λ λ³μμ κ°μ κ°μΌλ μ μ₯λλ λ©λͺ¨λ¦¬ μμΌλ‘λ κ°κ° μμΉ(λ©λͺ¨λ¦¬a,λ©λͺ¨λ¦¬b)κ° λ€λ₯Έ μνλΌ is λ κ±°μ§
  
  a = [1, 2, 3]
  b = a
  # λ λ³μκ° κ°(list)μ΄ κ°μΌλ―λ‘ == λ μ°Έ
  # λ λ³μμ κ°μ΄ μ μ₯λλ λ©λͺ¨λ¦¬λ κ°μ μμΉ(λ©λͺ¨λ¦¬a) μνλΌ is λ μ°Έ
  ```


---

- μΈμ€ν΄μ€ λ³μ
  - μΈμ€ν΄μ€κ° κ°μΈμ μΌλ‘ κ°μ§κ³  μλ μμ±(attribute)
  - κ° μΈμ€ν΄μ€λ€μ κ³ μ ν λ³μ


```python
class Person:
  	def __init__(self, name, age, gender): # name, age λ±μ΄ μΈμ€ν΄μ€
      	self.name = name	# name μΈμ€ν΄μ€ λ³μ μ μ
        self.age = age
        self.gender = gender

    def info(self):
      	return (self.name, self.age, self.gender)

hong = Person('νκΈΈλ', 100, 'M')	# name μΈμ€ν΄μ€ λ³μ ν λΉ
ko = Person('κ³ κΈΈλ', 40, 'M')

print(hong.info())
print(hong.name)	# name μΈμ€ν΄μ€ λ³μ μ κ·Ό
print(hong.age)
```

- μΈμ€ν΄μ€ λ©μλ

  - μΈμ€ν΄μ€ λ³μλ₯Ό μ¬μ©νκ±°λ, μΈμ€ν΄μ€ λ³μμ κ°μ μ€μ νλ λ©μλ
  - νΈμΆμ, μ²«λ²μ§Έ μΈμλ‘ μΈμ€ν΄μ€ μμ (self)μ΄ μ λ¬λ¨

- self

  - μΈμ€ν΄μ€ μμ 
  - νΈμΆ μ ()μ μ²«λ²μ§Έλ‘ μλ ₯λμ΄ μμ μ΄ μ λ¬λλλ‘ ν¨
  - νμ΄μ¬μ μλ¬΅μ  κ·μΉ

- μμ±μ(Constructor) λ©μλ

  - μΈμ€ν΄μ€ κ°μ²΄κ° μμ±λ  λ μλμΌλ‘ νΈμΆλλ λ©μλ

  ```python
  class Person:
      
      def __init__(self, name):
          print(f'μΈμ€ν΄μ€κ° μμ±λμμ΅λλ€. {name}')
          
  personl = Person('μ§λ―Ό')
  # μΈμ€ν΄μ€κ° μμ±λμμ΅λλ€. μ§λ―Ό
  ```

  

- μλ©Έμ(destructor) λ©μλ

  - μΈμ€ν΄μ€ κ°μ²΄κ° μλ©ΈλκΈ° μ§μ μ νΈμΆλλ λ©μλ

  ```python
  class Person:
      
      def __del__(self):
          print(f'μΈμ€ν΄μ€κ° μ¬λΌμ‘μ΅λλ€.')
          
  personl = Person()
  del personl
  # μΈμ€ν΄μ€κ° μ¬λΌμ‘μ΅λλ€
  ```

  
