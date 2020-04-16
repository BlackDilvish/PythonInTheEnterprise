import sys
import logging as log
from events import *


def log_settings():
    console = log.getLogger()
    console.setLevel(log.NOTSET)
    file = log.FileHandler("car_simulator_log.log")
    console.addHandler(file)


def print_menu():
    print("Press 1 to turn on the car")
    print("Press 2 to turn off the car")
    print("Press 3 to stop the car")
    print("Press 4 to turn right")
    print("Press 5 to turn left")
    print("Press 6 to fuel the car")
    print("Press 7 to speed up")
    print("Press 8 to slow down")
    print("Press 9 to drive into a tree")
    print("Press 10 to end simulation")


class Car:
    def __init__(self, car_brand):
        self.car_brand = car_brand
        self.car_started = False
        self.car_crashed = False
        self.car_fuel_flag = True
        self.velocity = 0
        self.wheel_angle = 0
        self.fuel_level = 50  # max 100

    def act(self, action):
        str = action().current_act(self)
        return str

    def start(self):
        if not self.car_started:
            self.car_started = True

    def turn_off(self):
        if self.car_started:
            self.car_started = False
            self.velocity = 0
            self.wheel_angle = 0

    def turn_right(self):
        if self.wheel_angle > -90:
            self.wheel_angle -= 2
            self.fuel_level -= 5

    def turn_left(self):
        if self.wheel_angle < 90:
            self.wheel_angle += 2
            self.fuel_level -= 5

    def speed_up(self):
        if self.velocity < 300:
            self.velocity += 30
            self.fuel_level -= 5
            return 1
        else:
            return 0

    def slow_down(self):
        if self.velocity > 0:
            self.velocity -= 30
            self.fuel_level -= 5
            return 1
        else:
            return 0

    def stop(self):
        self.velocity = 0

    def fuel_check(self):
        if self.fuel_level > 0:
            self.car_fuel_flag = True
        else:
            self.turn_off()
            self.car_fuel_flag = False

    def fuel_fill(self):
        if 100 > self.fuel_level > 0:
            self.fuel_level = 100
            self.car_fuel_flag = True
            return 1
        elif self.fuel_level <= 0:
            self.fuel_level = 100
            self.car_fuel_flag = True
            return 1
        else:
            return 0

    def drive_into_the_tree(self):
        self.car_crashed = True
        log.info("Car is crashed!")
        log.info("End of simulation!")
        print("End of simulation!")
        sys.exit(0)

    def print_total_info(self):
        log.info("Car brand: " + str(self.car_brand) + " Velocity: " + str(self.velocity) + " Wheels angle: " + str(
            self.wheel_angle) + " Fuel level: " + str(self.fuel_level))


class Environment:
    def __init__(self, car):
        print("Hello in my simple car simulator!")
        self.car = car
        self.events_to_choose = {
            1: CarStart,
            2: CarTurnOff,
            3: CarStop,
            4: TurnRight,
            5: TurnLeft,
            6: FuelCar,
            7: SpeedUp,
            8: SlowDown,
            9: MakeACrash,
            10: CloseSimulation
        }

    def start(self):
        print_menu()
        while True:
            opt = int(input("Choose an action to make: "))
            if 0 < opt < 11:
                action = self.events_to_choose[opt]
                str = self.car.act(action)
                print(str)
                self.car.print_total_info()
            else:
                print("Choose right option!")


if __name__ == '__main__':
    log_settings()
    if len(sys.argv) == 2:
        envrmnt = Environment(Car(sys.argv[1]))
        envrmnt.start()
    else:
        envrmnt = Environment(Car("BMW"))
        envrmnt.start()