# Дано натуральное число. Найдите цифру, стоящую в разряде десятков в его десятичной записи (вторую справа цифру).

num = int(input())

print(num % 100 // 10)
