import random

arr = [random.randint(1, 999) for i in range(20)]

print(arr)

def asc(a, b):
    return a > b

def desc(a, b):
    return a < b


def evenFirst(a, b):
    if a % 2 == 1 and b % 2 == 0:
        return True
    if a % 2 == 0 and b % 2 == 1:
        return False
    return asc(a, b)


def lastNumber(a, b):
    if a % 10 > b % 10:
        return True
    if a % 10 == b % 10 and a > b:
        return asc(a, b)


def bubbleSort(list, method=asc):
    for i in range(len(list) - 1):
        for j in range(len(list) - 1 - i):
            if method(list[j], list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]




#bubbleSort(arr, lambda a, b:a<b)
arr.sort(key=lambda a: a%10)
print(arr)

arr2 = [[random.randint(1, 20) for j in range(5)] for i in range(5)]


def hello():
    print("Hello")

def goodbye():
    print("Good bye")

message = hello
message()

message = goodbye
message()

mess = [hello, goodbye]
for f in mess:
    f()


def summ(a, b):
    return a+b

def diff(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

'''operation = [summ, diff, mult, div]
a = float(input("a = "))
b = float(input("b = "))
oper = int(input("1+, 2-, 3*, 4/ :"))
res = operation[oper-1](a,b)
print(res)'''


def kopatel():
    print("Копає один працівник")


def kopatel3():
    print("Копають три працівники з лопатою і перфоратором")


def exkavator():
    print("Копає екскаватор, працівники курять в сторонці")


def prorab(length):
    if length < 100:
        return kopatel
    if length < 500:
        return kopatel3
    return exkavator


director = prorab(1500)
director()
