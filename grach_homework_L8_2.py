class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def data_inp():
    while True:
        x = input("\nВведите через пробел числитель и знаменатель: ").split()
        if len(x) != 2:
            print("\n*** Введено не два числа, прошу повторить.")
            continue
        try:
            a, b = int(x[0]), int(x[1])
            break
        except:
            print("\n*** Ошибка ввода, прошу повторить.")
    return a, b


count = 0
while True:
    try:
        x, y = data_inp()
        if y == 0:
            raise OwnError("*** Знаменатель равен 0 !  Придется повторить ввод...")
    except OwnError as err:
        print(err)
    else:
        print(f"\n{x} / {y} = {x / y}")
        break
    finally:
        count += 1

print(f"\nСпасибо, всего попыток деления: {count}.")