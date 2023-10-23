'''n = int(input("n = "))
d = 0
s = 0
while s < n:
    s += 4
    d += 1
    if s >= n:
        break
    else:
        s -= 2

print(d)'''


'''n = int(input("n = "))
f1 = 0
f2 = 1

k = 2
if n < 3:
    print(n - 1)
else:
    while k != n:
        k += 1
        fn = f1 + f2
        f1 = f2
        f2 = fn
    print(fn)'''


'''n = int(input("n = "))
f1 = 0
f2 = 1
fn = f1 + f2
k = 2
while fn != n:
    k += 1
    fn = f1 + f2
    f1 = f2
    f2 = fn

print(k)'''


n = int(input("n = "))
s = 0
while n > 0:
    r = n % 10
    s += r
    n //= 10

print(s)

