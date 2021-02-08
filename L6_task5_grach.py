class Stationery:
    def __init__(self, title):
        self.ttl = title
        # print(f"Init data: title - {title}")

    def draw(self):
        print("\nЗапуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("\nDraw by Pen")


class Pencil(Stationery):
    def draw(self):
        print("\nDraw by Pencil")


class Handle(Stationery):
    def draw(self):
        print("\nDraw by Handle")


Original = Stationery('stationery')
Original.draw()
My_pen = Pen("Checking pen")
My_pen.draw()
My_pencil = Pencil("Checking pencil")
My_pencil.draw()
My_handle = Handle("Checking pencil")
My_handle.draw()