
'''
while condition:
    oper
    oper
    oper
'''

'''a = 1
while a < 6:
    print(a)
    a += 1'''

'''a = int(input())
b = int(input())
k = 0
while a >= b:
    a -= b
    k += 1

print(a) # a % b
print(k) # a // b'''


#Дано целое число N (> 0). Если оно является степенью числа 3, то вы-
#вести True, если не является — вывести False.

import math

'''n = int(input())
k = 1
while k < n:
    k *= 3

if k == n:
    print("True")
else:
    print("False")'''



#Дано целое число N (> 0), являющееся некоторой степенью числа 2:
#N = 2**K . Найти целое число K — показатель этой степени.

'''n = int(input())
p = 1
k = 0
while p < n:
    p *= 2
    k += 1

print(k)'''


#Дано целое число N (> 0). Найти наименьшее целое положительное
#число K, квадрат которого превосходит N: K*K > N. Функцию извлечения
#квадратного корня не использовать.

n = int(input())
k = 1
while k*k < n:
    k += 1

print(k)
