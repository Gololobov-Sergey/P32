import string

st = "Білецький Денис"
'''st1 = "papa"
print(st + st1)
print(st[-2])
print(len(st))
print(st.find("am", 4))
l = ["1", "2", "3"]
print(" * ".join(l))
print(st.count('am'))
#print(st.index("Денис"))
print(st.capitalize())
print(st.title())
print(st.rfind('и'))
print(st.replace('и', '#', 2))
print(st.split('с '))
print(st.isalnum())
print(st.isalpha())
print(st.isdigit())
print(st.islower())
print(st.isupper())
print(st.center(50, '.'), "sfsdf")
print(st.ljust(50), "sfsdf")
print(st.rjust(50), "sfsdf")
a = 598
str(a)

print(st[::-1])'''

p = st.find(' ')
#st = st[p+1:] + " " + st[:p]
#print(st)
st = " ".join(st.split()[::-1])

# Користувач вводить із клавіатури рядок. Порахуйте кількість букв, цифр у рядку.
# Виведіть обидва результати на екран.

'''s = input()
d = b = 0
for i in s:
    if i.isdigit():
        d += 1
    elif i.isalpha():
        b += 1
print(d)
print(b)'''

# Дан символ C и строка S. Удвоить каждое вхождение символа C
# в строку S.


'''print(string.punctuation)
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)'''

# Дана строка-предложение. Вывести самое короткое
# слово в предложении. Если таких слов несколько, то вывести последнее из
# них. Словом считать набор символов, не содержащий пробелов, знаков
# препинания и ограниченный пробелами, знаками препинания

st = "Словом считать набор символов, не содержащий пробелов, знаков."
words = st.split()
minLen = len(words[0])
ind = 0
for i in range(len(words)):
    for s in string.punctuation:
        if s in words[i]:
            words[i] = words[i].replace(s,'')
    if len(words[i]) <= minLen:
        minLen = len(words[i])
        ind = i

print(words[ind])


# Дана строка, изображающая арифметическое выражение вида
# «<цифра>±<цифра>±...±<цифра>», где на месте знака операции «±» находится
# символ «+» или «–» (например, «4+7–2–8»). Вывести значение данного
# выражения (целое число).


st = "4+3+2-1-1-1"
a = int(st[0])
for i in range(1, len(st), 2):
    oper = st[i]
    b = int(st[i+1])
    if oper == '+':
        a += b
    else:
        a -= b

print(a)