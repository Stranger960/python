class Road:
    def __init__(self, length, width):
        self._len = length
        self._wdt = width
        #print("Init: length =>", length, "width =>", width)

    def calc(self,length, width):
        print (f"\nРазмеры участка: {length} x {width} кв м ")
        base = 25*5                                # weight for 1sq m, kilo
        return base * length * width / 1000

CaseRoad = Road(10,10)
print(f"Масса необходимого асфальта: {int(CaseRoad.calc(20, 5000))} тонн")