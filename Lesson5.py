'''M = int(input("M, l = "))
if M > 0:
    P = int(input("P, % = "))
    if P >= 0 and P <= 100:
        k1 = 1000 * M * P / 100
        k2 = int(input("k2, ml = "))
        if k2 >=0 and k2 <= 1000 * M - k1:
            k3 = 1000 * M - k1 - k2
            if k1 > k3:
                print("k1 > k3")
            elif k1 < k3:
                print("k1 < k3")
            else:
                print("k1 = k3")
        else:
            print("K2 not correct!")
    else:
        print("P not correct!")
else:
    print("M not correct!")'''


#Даны два целых числа: D (день) и M (месяц), определяющие правиль-
#ную дату невисокосного года. Вывести значения D и M для даты, следую-
#щей за указанной.

#D = int(input("D = "))
#M = int(input("M = "))

'''D += 1

if M == 4 or M == 6 or M == 9 or M == 11:
    Dmax = 30
elif M == 2:
    Dmax = 28
else:
    Dmax = 31

if D > Dmax:
    D = 1
    M += 1

M %= 12

print(f"{D}.{M}")'''

'''D -= 1
if D == 0:
    M -= 1
    if M == 4 or M == 6 or M == 9 or M == 11:
        D = 30
    elif M == 2:
        D = 28
    else:
        D = 31

if M == 0:
    M = 12

print(f"{D}.{M}")'''


# Локатор ориентирован на одну из сторон света («С» — север, «З» —
# запад, «Ю» — юг, «В» — восток) и может принимать три цифровые ко-
# манды поворота: 1 — поворот налево, –1 — поворот направо, 2 — поворот
# на 180°. Дан символ C — исходная ориентация локатора и целые числа N1
# и N2 — две посланные команды. Вывести ориентацию локатора после вы-
# полнения этих команд.

dir = input("Поточне положення ( N, E, S, W ) - ")
com1 = int(input("Команда 1 : "))
com2 = int(input("Команда 2 : "))

if dir == "N":
    pos = 0
elif dir == "W":
    pos = 1
elif dir == "S":
    pos = 2
else:
    pos = 3

pos += com1
pos += com2

pos += 4
pos %= 4

if pos == 0:
    dir = "N"
elif pos == 1:
    dir = "W"
elif pos == 2:
    dir = "S"
else:
    dir = "E"

print(dir)