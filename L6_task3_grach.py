class Worker:
    income = {"wage": 0, "bonus": 0}

    def __init__(self, name, surname, position, income):
        self.nam = name
        self.surn = surname
        self.pos = position
        self._inc = income


class Position(Worker):
    def get_full_name(self, name, surname):
        print(f"\nПолное имя: {name} {surname}")

    def get_total_income(self, income):
        print(f"Доход: {income['wage'] + income['bonus']} руб")


inc = {"wage": 50000, "bonus": 10000}
Pos_1 = Position("", "", "", inc)

Pos_1.get_full_name("Петр", "Иванов")
Pos_1.get_total_income(inc)