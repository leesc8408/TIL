import random
re = 5

for i in range(re):
    num = random.sample(range(1,46), 6)
    num.sort()
    print(num)
