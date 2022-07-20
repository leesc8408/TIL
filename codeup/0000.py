class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def circumference(self):
        return 2 * (self.x + self.y)

r1 = Rectangle(10, 30)
print(r1.area())
print(r1.circumference())

r2 = Rectangle(300, 20)
print(r2.area())
print(r2.circumference())


my_list = [1, 3, 2]
# 리스트의 데이터를 직접 정렬
my_list.sort()
print(my_list)

my_list = [5, 4, 6]
# 리스트는 sorted 함수의 값으로 전달(사용)될 뿐
sorted(my_list)
print(my_list)
