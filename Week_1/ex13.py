# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (пробелы важны!).
# Нельзя пользоваться конкатенацией строк (используйте print с несколькими параметрами).

num = int(input())

print('The next number for the number', num, 'is', num + 1, end='.\n')
print('The previous number for the number', num, 'is', num - 1, end='.')
