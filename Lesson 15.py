import random

students = [['Student ' + str(i+1)] for i in range(10)]
for s in students:
    s.append([random.randint(7, 12) for j in range(10)])

#print(students)
def best_student(students):
    i = 0
    maxMark = sum(students[0][1])
    for s in students:
        #print(sum(s[1]))
        if sum(s[1]) > maxMark:
            maxMark = sum(s[1])
            i = students.index(s)
    return i

#print(best_student(students))

def func(a, b=5, c=5):
    print(a+b+c)

#func(1,10)

def func1(*args, **kwargs):
    print(type(args))
    print(type(kwargs))
    for i in args:
        print(i)
    for w, v in kwargs.items():
        print(w, v)
    print(kwargs["name"])


#func1(1,2,4,5,6.345, "345")
#func1(1,2,4,5,6.345, "345", name="sdfsd", count=3)

def summ(*value):
    s = 0
    for i in value:
        s += i
    return s

#print(summ(1,2,3,4,5,6,7,8,9,10))


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

def number(n):
    print(n, end=' ')
    if n > 1:
        number(n-1)

def number1(n):
    if n > 1:
        number1(n-1)
    print(n, end=' ')

number1(5)


def sum2(a, b):
    if a == b:
        return b
    return a + sum2(a+1, b)

print(sum2(3,8))