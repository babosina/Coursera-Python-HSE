# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.

rub = int(input())
cop = int(input())
cake = int(input())

print((rub * cake + (cop * cake) // 100), cop * cake % 100)
