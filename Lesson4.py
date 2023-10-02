'''a = int(input())
if a > 0:
    a += 1
elif a < 0:
    a -= 2
else:
    a = 10
print(a)'''


'''a = int(input())
b = int(input())
c = int(input())'''

'''if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
    print(c)'''

'''res = 1
if a > 0:
    res += 1
if b > 0:
    res += 1
if c > 0:
    res += 1
print(res)'''

'''if c < b and c < a:
    print(a + b)
elif b < c and b < a:
    print(a + c)
else:
    print(c + b)'''


'''m = int(input("m = "))
z1 = int(input("z1 = "))
z2 = int(input("z2 = "))
z = 1000*z1 + z2
k = 1000*m - z
if k > z:
    print("K")
else:
    print("Z")
print(k)
print(z)'''


'''a = int(input())
if a == 0:
    print("0")
else:
    if a > 0:
        print("Додатне", end=' ')
    else:
        print("Від'ємне", end=' ')

    if a % 2 == 0:
        print("парне", end=' ')
    else:
        print("не парне", end=' ')
    print("число")'''

year = int(input())
print(365 + int(year % 4 == 0 and year % 100 != 0 or year % 400 == 0))