import random

'''a0 = 5
d = 8
arr = [a0 + i*d for i in range(10)]
#arr = [1,4,7,11,13]
d = arr[1] - arr[0]
is_progress = True
for i in range(1, len(arr)-1):
    if arr[i+1] - arr[i] != d:
        is_progress = False
        break

print(is_progress)'''

# Дан массив A размера N. Найти минимальный элемент из его элемен-
# тов с четными номерами: A2, A4, A6, ... .

'''arr = [random.randint(1, 10) for i in range(10)]
print(arr)
maxValue = arr[0]
for i in range(0, len(arr), 2):
    print(arr[i], end=' ')
    if arr[i] < maxValue:
        maxValue = arr[i]
print()
print(maxValue)'''

# Дан массив размера N. Найти номера тех элементов массива, которые
# больше своего правого соседа, и количество таких элементов. Найденные
# номера выводить в порядке их возрастания.

n = int(input("n = "))
arr = [random.randint(1, 50) for i in range(n)]
print(arr)



'''k = 0
for i in range(len(arr)-1):
    if arr[i] > arr[i+1]:
        print(i, end=" ")
        k += 1
print()
print(k)'''

'''for i in range(10, -1, -1):
    for j in range(n):
        if i < arr[j]:
            print("#  ", end='')
        else:
            print("   ", end='')

    print()
for i in range(n):
    print(f"{i:<3}", end='')

print()
maxTemp = 0
h = 0
for i in range(len(arr)-1):
    if abs(arr[i] - arr[i+1]) > maxTemp:
        maxTemp = abs(arr[i] - arr[i+1])
        h = i
print(h)'''

# Дано число R и массив A размера N. Найти элемент массива, который
# наиболее близок к числу R

'''r = int(input("r = "))
dif = abs(r - arr[0])
pos = 0
for i in range(len(arr)):
    if abs(r - arr[i]) < dif:
        dif = abs(r - arr[i])
        pos = i
print(pos)
print(arr[pos])'''


# Дан целочисленный массив размера N, содержащий ровно два одина-
# ковых элемента. Найти номера одинаковых элементов и вывести эти номе-
# ра в порядке возрастания.

