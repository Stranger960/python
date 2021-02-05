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