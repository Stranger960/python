class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

lst = []
while True:
    inp = input("\nВведите очередное число ('stop' для завершения): ")
    if len(inp.split()) != 1:
        print("\n*** Введено не одно значение, прошу повторить.")
        continue
    elif inp == "stop":
        break
    else:
        try:
            if  not inp.isnumeric():
                raise OwnError("*** Введено не число !  Придется повторить ввод...")
        except OwnError as err:
            print(err)
        else:
            lst.append(float(inp))
        finally:
            pass

print(f"\nСпасибо, всего введено значений: {len(lst)}.")
print(f"Окончательный список: {lst}.")