'''n = 5
for k in range(3):
    for i in range(k+3):
        for j in range(n - i + 1 - k):
            print(" ", end='')
        for j in range(2*(i + k) + 1):
            if (j == 0 or j == 2*(i + k)) and i == k+2:
                print("#", end='')
            else:
                print("*", end='')
        print()
for i in range(2):
    for j in range(5):
        print(" ", end='')
    print("***")'''

'''c = 0
for h in range(24):
    for m in range(60):
        h1 = h // 10
        h2 = h % 10
        m1 = m // 10
        m2 = m % 10
        if h1 == m2 and h2 == m1:
            print(f"{h1}{h2}:{m1}{m2}")
            c += 1
print(c)'''


'''for i in range(0, 11):
    if i != 0:
        print(f"{i:4}", end='')
    else:
        print(f"    ", end='')
print()
for i in range(1, 11):
    print(f"{i:4}", end='')
    for j in range(1, 11):
        print(f"{i*j:4}", end='')
    print()'''

'''A = int(input("A = "))
B = int(input("B = "))
C = int(input("C = "))
k = 0
while A >= C:
    M = B
    while M >= C:
        k += 1
        M -= C
    A -= C

print(k)'''

import math
R = int(input("R = "))
r = int(input("r = "))
h = int(input("h = "))
k = 0
for x in range(-R, R+1, h):
    for y in range(-R, R+1, h):
        l = math.sqrt(x*x + y*y)
        if l > r and l < R:
            k+=1
print(k)