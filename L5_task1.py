inp = "?"
try:
    with open("d:\my_text.txt", "w", encoding="utf-8") as fout:
        while inp:
            inp = input("\nВведите данные => ")
            print(inp, file=fout)
except IOError as err:
    print(f"\nОшибка вводва: {err}")