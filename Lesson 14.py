
def printLine(symbol='*', count=10):
    for i in range(count):
        print(symbol, end='')
    print()

printLine('#', 50)
printLine('#')
printLine(count=50)
printLine()


def add(a, b):
    c = a + b
    return c

printLine('*', 10)
printLine('*', 10)

s = add("5", "5")
print(s)

def isEven(a):
    return a % 2 == 0

def avg3(a,b,c):
    return (a+b+c)/3


c = 0
l = [1,2,3,4,5,6]
for i in l:
    if isEven(i):
        c += 1

print(10 + avg3(3,4,5))