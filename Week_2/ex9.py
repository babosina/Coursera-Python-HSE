"""
Для данного числа n<100 закончите фразу “На лугу пасется...” одним из возможных продолжений:
“n коров”, “n корова”, “n коровы”, правильно склоняя слово “корова”.
"""

n = int(input())

if 11 <= n <= 14:
    print(n, 'korov')
else:
    rem = n % 10
    if rem == 0 or (5 <= rem <= 9):
        print(n, 'korov')
    if rem == 1:
        print(n, 'korova')
    if 2 <= rem <= 4:
        print(n, 'korovy')
