import random
a = []
b = []
c = []
for i in range(9):#через рандом заполняю чтобы интереснее было
    d = random.randint(1, 50)
    a.append(d)
for i in a:
    if i in b:
        if i not in c:
            c.append(i)
    else:
        b.append(i)
if c:
    print(f"Список: {a}\nПовторяющиеся числа: {c}")
else:
    print(f"Список: {a}\nПовторяющихся чисел нет.")