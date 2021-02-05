"""
6. Необходимо создать (не программно) текстовый файл, 
где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

try:
    with open("text_6.txt", "r", encoding="utf-8") as fin:
        cont = fin.read().replace("-", "0").replace("(пр)", "").replace("'","")
        w = cont.replace("(лаб)", "").replace("(л)","").replace("\n"," ")
except IOError as err:
        print(f"\nОшибка чтения: {err}")
print("\nИсходные данные:\n",cont)

z = list(w.split(" "))
dict ={}
for k in range(0,len(z),4):
    s = sum(list(map(int,z[k+1:k+4])))
    dict[z[k]]= s
print ("\nСформирован словарь: ",dict)



"""
for line in w:
    words = line.split()
    names.append(words[1])
"""










"""
for k in range(0,len(cont),4):
    dict[k] =  
    print(cont[k])

try:
    with open("new_file.txt", "w", encoding="utf-8") as fout:
        [print (str(z) + " ", file=fout, end = "") for z in range(10)]
except IOError as err:
    print(f"\nОшибка записи: {err}")

summ = 0
try:
    with open("new_file.txt", "r", encoding="utf-8") as fin:
        cont = fin.read().replace(" ", "")
except IOError as err:
    print(f"\nОшибка чтения: {err}")
for k in cont:
    summ += int(k)
print("\nСумма: ", summ)


w = [_.split() for _ in cont]
lst = [str(x).replace(k, my_dct[k]) for x in w for k in my_dct.keys() if k == (x[0])]
"""
