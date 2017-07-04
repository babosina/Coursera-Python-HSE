"""
В доме несколько подъездов.
В каждом подъезде одинаковое количество квартир.
Квартиры нумеруются подряд, начиная с единицы.
Может ли в некотором подъезде первая квартира иметь номер x, а последняя – номер y?
"""

x = int(input())
y = int(input())

if y % (y - x + 1) == 0 or x == 1:
    print('YES')
else:
    print('NO')