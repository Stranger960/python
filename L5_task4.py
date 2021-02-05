my_dct = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
try:
    with open("text_4.txt", "r", encoding="utf-8") as fin:
        cont = fin.readlines()
except IOError as err:
    print(f"\nОшибка чтения: {err}")
w = [_.split() for _ in cont]
lst = [str(x).replace(k, my_dct[k]) for x in w for k in my_dct.keys() if k == (x[0])]
try:
    with open("my_file.txt", "w", encoding="utf-8") as fout:
         [ print (z[2:-2].replace("'", "").replace(",", ""), file = fout) for z in lst]
except IOError as err:
    print(f"\nОшибка записи: {err}")