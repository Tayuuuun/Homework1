
d1 = int(input("Введите целое число: "))

digit = d1 % 10
d2 = digit

d1 = d1 // 10

while d1 > 0:
    digit = d1 % 10
    d1 = d1 // 10
    d2 = d2 * 10
    d2 = d2 + digit

print( d2)