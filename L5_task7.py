import json

try:
    with open("text_7.txt", "r", encoding="utf-8") as fin:
        cont = fin.read().replace("\n", " ").split(" ")
except IOError as err:
    print(f"\nОшибка чтения: {err}")

dict = {}
for k in range(0, len(cont), 4):
    dict[(cont[k] + " " + cont[k + 1])] = int(cont[k + 2]) - int(cont[k + 3])
print ("\nСловарь фирм:", dict)

rev, cou = 0., 0
for m in dict.keys():
    if dict[m] <= 0:
        continue
    cou += 1
    rev += dict[m]
avrg = rev / cou
print ("Cредняя прибыль: ", avrg)

lst = [dict, {"average revenue": avrg}]
print ("Объединяем в список:\n", lst)
print ("Сериализуем и записываем в файл:  jsn_dump.json")
with open("jsn_dump.json", "w") as fout:
    json.dump(lst, fout)