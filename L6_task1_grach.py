from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.col = color
        print("init color =", color)

    def running(self, color):
        dct = {"red": 7, "yellow": 2, "green": 3}
        for k in dct.keys():
            if k == color:
                print("Color: ", k, "   Duration: ", dct[k])
                sleep(dct[k])


Semafor = TrafficLight("white")

for _ in range(5):
    print("\nRound => ", _, "out of 5")
    for light in ("red", "yellow", "green"):
        Semafor.running(light)
