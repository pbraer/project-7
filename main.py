print("""
Project #7 Составление отчетов успеваемости и посещаемости студентов
Разработчик:
Браер П.С.

""")

#data input
students = []
print('Введите имена студентов:')
s = input()
while s != '':
    students.append(s)
    s = input()
students = sorted(students)

print('\033[1m' + '''





'+' - студент присутствовал на занятии
'н' - студент присутствовал на занятии
'x' - студент работал на уроке и получил х баллов (макс. - 5 баллов/занятие)
''' + '\033[0m')

mx = 0
for n in students:
    if len(n) >= mx:
        mx = len(n)
print(' ' * (mx+4), sep='', end='')
print('\033[1m' + '01.04.2021    08.04.2021    15.04.2021    22.04.2021    29.04.2021' + '\033[0m')

marks_inf = {}
miss_inf = {}
for s in students:
    print('\033[1m' + s + '\033[0m', ' ' * (17 - len(s)), sep='', end='')
    marks = []
    str_marks = input()
    st = list(str_marks)
    for e in st:
        if e != ' ':
            marks.append(e)
    miss = 0
    mark_sum = 0
    for m in marks:
        if m == 'н':
            miss += 1
        elif m.isdigit() == True:
            mark_sum += int(m)
    marks_inf[s] = mark_sum
    miss_inf[s] = miss

list_mark_inf = list(marks_inf.items())
list_mark_inf.sort(key=lambda i: i[1], reverse = True)


#score rating
print('\033[1m' + '''



Рейтинг студентов:

Имя                               Баллы''' + '\033[0m')
i = 0
for name in list_mark_inf:
    i += 1
    print(i, '.', sep='', end=' ')
    print(name[0], ' ' * (31 - len(name[0])), name[1], ' ' * (7 - len(str(name[1]))) + '(', round((int(name[1])/25) * 100), '%)', sep='')


list_miss_inf = list(miss_inf.items())
ex = []
good = []
so = []
bad = []
for name in list_miss_inf:
    m = int(name[1])
    if m == 0:
        ex.append(name[0])
    elif m == 1 or m == 2:
        good.append(name[0])
    elif m == 3 or m == 4:
        so.append(name[0])
    elif m == 5:
        bad.append(name[0])


#attendance rating
print('\033[1m' + '''



Посещаемость:
''' + '\033[0m')

if len(ex) != 0:
    print('\033[1m' + 'Посетили все занятия:' + '\033[0m', ' ' * (34 - len('Посетили все занятия:')), sep='', end='')
    n = 0
    for name in ex:
        n += 1
        if n != len(ex):
            c = ','
        else:
            c = ''
        print(name, c, sep='', end=' ')
    print('')

if len(good) != 0:
    print('\033[1m' + 'Хорошая посещаемость:' + '\033[0m', ' ' * (34 - len('Хорошая посещаемость:')), sep='', end='')
    n = 0
    for name in good:
        n += 1
        if n != len(good):
            c = ','
        else:
            c = ''
        print(name, c, sep='', end=' ')
    print('')

if len(so) != 0:
    print('\033[1m' + 'Изредка посещали:' + '\033[0m', ' ' * (34 - len('Изредка посещали:')), sep='', end='')
    n = 0
    for name in so:
        n += 1
        if n != len(so):
            c = ','
        else:
            c = ''
        print(name, c, sep='', end=' ')
    print('')

if len(bad) != 0:
    print('\033[1m' + 'Не посетили ни одного занятия:' + '\033[0m', ' ' * (34 - len('Не посетили ни одного занятия:')), sep='', end='')
    n = 0
    for name in bad:
        n += 1
        if n != len(bad):
            c = ','
        else:
            c = ''
        print(name, c, sep='', end=' ')
    print('')
