'''print(5 > 4)
res = 5 > 5
res = 5 < 5
res = 5 >= 5
res = 5 <= 5
res = 5 != 5
res = 5 == 5

a = 5
b = 4

print(not a)
print(res)

print(True and True)
print(True and False)
print(False and True)
print(False and False)
print()

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(5 > 3 or 4 != 4 and 4 == 4 or 5 != 3)

print()

print(True ^ True)
print(True ^ False)
print(False ^ True)
print(False ^ False)'''


'''a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
d = int(input("d = "))

#res = a % 2 == b % 2

#res = a > b > c or c > b > a
res = (a > 0) + (b > 0) + (c > 0) + (d > 0) == 2
print(res)'''


x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

print((x1 + y1) % 2 == 0)
print(x1 == x2 or y1 == y2)
print(abs(x2 - x1) == abs(y2 - y1))
print(abs(x2 - x1) == abs(y2 - y1) or x1 == x2 or y1 == y2)