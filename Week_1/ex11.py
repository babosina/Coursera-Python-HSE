# Дано число N. С начала суток прошло N минут.
# Определите, сколько часов и минут будут показывать электронные часы в этот момент.

minutes = int(input())

print(minutes // 60 % 24, minutes % 60)
