# В этой задаче необходимо проверить, делится ли число A на число B нацело.
# Использовать можно только арифметические операции, использование любых видов ветвлений, функций и т.п. запрещено.

a = int(input())
b = int(input())

x = a % b == 0

print('YES' * x + 'NO' * (1 - x))