'''a = 5 #int
print(a)
a = "mama"
print(a)

b = 2.2 # float

s = "mama" #str

f1 = True #bool
f2 = False


# + - * / ** // % += -= *= /= %= //= **=

2 * 2 ** 2
print(5//2)'''

'''a = 5
b = 4
#a += b
a **= 2
print(a)'''

'''a = int(input("Введить а: "))
b = float(input("Введить b: "))
c = a + b
print(c)'''

# Даны три точки A, B, C на числовой оси. Найти длины отрезков AC
# и BC и их сумму.
A = int(input("A : "))
B = int(input("B : "))
C = int(input("C : "))
AC = abs(C - A)
BC = abs(C - B)
AC_BC = AC + BC
print(AC)
print(BC)
print(AC_BC)



# Даны три точки A, B, C на числовой оси. Точка C расположена между
# точками A и B. Найти произведение длин отрезков AC и BC.


# Даны целые положительные числа A и B (A > B). На отрезке длины A
# размещено максимально возможное количество отрезков длины B (без на-
# ложений).