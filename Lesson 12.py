import random

'''l = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(l[0][1])

print()

for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=' ')
    print()

print()

for i in l:
    for j in i:
        print(j, end=' ')
    print()'''

row = 4 #int(input("row = "))
col = 6 #int(input("col = "))
arr2 = [[random.randint(1, 9) for j in range(col)] for i in range(row)]
list_sum=[]
for li in arr2:
    sumRow = 0
    for elem in li:
        sumRow += elem
        print(f"{elem:>3}", end='')
    print("|", sumRow)
    list_sum.append(sumRow)
print("------------------")
for j in range(col):
    sumCol = 0
    for i in range(row):
        sumCol += arr2[i][j]
    print(f"{sumCol:>3}", end='')

for i in range(len(list_sum)-1):
    for j in range(len(list_sum)-1-i):
        if list_sum[j] < list_sum[j+1]:
            list_sum[j], list_sum[j+1] = list_sum[j+1], list_sum[j]
            arr2[j], arr2[j+1] = arr2[j+1], arr2[j]

print()
print()

for li in arr2:
    sumRow = 0
    for elem in li:
        sumRow += elem
        print(f"{elem:>3}", end='')
    print("|", sumRow)
print("------------------")
for j in range(col):
    sumCol = 0
    for i in range(row):
        sumCol += arr2[i][j]
    print(f"{sumCol:>3}", end='')

'''a = 5
b = 8
a, b = b, a'''


'''arr = [random.randint(1, 50) for i in range(10)]
#print(arr)
#arr[0], arr[len(arr)-1] = arr[len(arr)-1], arr[0]
#print(arr)

k = 0
for i in range(len(arr)-1):
    for j in range(len(arr)-1-i):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            k += 1
#print(arr)
print(k)'''



'''print(arr)
arr2 = arr.copy()
arr2[0] = 100
print(arr)
arr.sort()
sorted(arr)'''