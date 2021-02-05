try:
    with open("text_3.txt", "r", encoding="utf-8") as fin:
       cont = fin.readlines()
except IOError as err:
    print(f"\nОшибка: {err}")

summ = 0.
print("\nСотрудники с окладом менее 20 тыс:")
for k in [w.split() for w in cont]:
    summ += float(k[1])
    if float(k[1]) < 20000.:
        print(k[0])
print ("\nCредняя величина дохода сотрудников: ",summ/len(cont),"руб")