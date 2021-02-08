from random import random as rnd

class Car:
    is_police = True
    def __init__(self, speed, color, name, is_police):
        self.spd = speed
        self.clr = color
        self.nam = name
        self.is_P = is_police
        #print(f"Init data: speed - {speed}, color - {color}, name - {name}, is_police - {is_police}")

    def go(self):
        print("Car is running...")

    def stop(self):
        print("Car stopped...")

    def turn(self, dir):
        print("Car is turning ", dir)

    def show_speed(self):
        speed = rnd() * 200
        return speed


class TownCar(Car):
    def show_speed(self):
        speed = 20+ rnd() * 50
        if speed > 60:
            print("Speed limitation exceeded !!!")
        return speed


class WorkCar(Car):
    def show_speed(self):
        speed = rnd() * 200
        if speed > 40:
            print("Speed limitation exceeded !!!")
        return speed


SportCar = Car(200, "red", "Ferrari", False)
PoliceCar = Car(180, "white", "Ford", True)

print(f"\nSportCar:")
SportCar.go()
SportCar.turn("left")
SportCar.turn("right")
SportCar.stop()

TownCar(100, "green", "Nissan", False)
WorkCar(80, "black", "Honda", False)

print(f"\nWorkCar:")
v = WorkCar.show_speed(100)
print ("WorkCar Speed: ",round(v,1))

print(f"\nTownCar:")
w = TownCar.show_speed(30)
print ("TownCar Speed: ",round(w,1))
