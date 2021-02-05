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