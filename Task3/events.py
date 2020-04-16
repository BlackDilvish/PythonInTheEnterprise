from abc import ABC
import sys


class Event(ABC):
    def current_act(self, car):
        pass


class CarStart(Event):
    def current_act(self, car):
        car.start()
        return str("Car is turned on!")


class CarTurnOff(Event):
    def current_act(self, car):
        car.turn_off()
        return str("Car is turned off!")


class CarStop(Event):
    def current_act(self, car):
        car.stop()
        return str("Car is stopped!")


class TurnRight(Event):
    def current_act(self, car):
        if car.car_fuel_flag:
            if car.car_started:
                car.turn_right()
                car.fuel_check()
                return str("Turning right!")
            else:
                return str("You have to turn on your car first!")
        else:
            return str("You can't move on! Out of fuel!")


class TurnLeft(Event):
    def current_act(self, car):
        if car.car_fuel_flag:
            if car.car_started:
                car.turn_left()
                car.fuel_check()
                return str("Turning left!")
            else:
                return str("You have to turn on your car first!")
        else:
            return str("You can't move on! Out of fuel!")


class FuelCar(Event):
    def current_act(self, car):
        if car.fuel_fill():
            return str("Car is fueled")
        else:
            return str("This is not necessary at this moment!")


class SpeedUp(Event):
    def current_act(self, car):
        if car.car_fuel_flag:
            if car.car_started:
                if car.speed_up():
                    car.fuel_check()
                    return str("Speeding up!")
                else:
                    return str("You cant go faster! That's the car limit!")
            else:
                return str("You have to turn on your car first!")
        else:
            return str("You can't move on! Out of fuel!")


class SlowDown(Event):
    def current_act(self, car):
        if car.car_fuel_flag:
            if car.car_started:
                if car.slow_down():
                    car.fuel_check()
                    return str("Slowing down!")
                else:
                    return str("Car is stopped!")
            else:
                return str("You have to turn on your car first!")
        else:
            return str("You can't move on! Out of fuel!")


class MakeACrash(Event):
    def current_act(self, car):
        if car.car_started:
            car.drive_into_the_tree()
            return str("End of simulation")
        else:
            return str("You have to turn on your car first!")


class CloseSimulation(Event):
    def current_act(self, car):
        print("End of simulation!")
        sys.exit(0)