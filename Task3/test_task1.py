#Using kamilsudol be5820ba6ab1a4e3005dd4243d931b2f3cbcde88
import unittest
import task
import events

class Tests(unittest.TestCase):
    def setUp(self):
        self.car = task.Car("Opel")

    def test_turn_start(self):
        self.car.start()
        self.assertEqual(True, self.car.car_started)

    def test_turn_off(self):
        self.car.turn_off()
        self.assertEqual(False, self.car.car_started)

    def test_turn_right(self):
        self.car.start()
        self.car.turn_right()
        self.assertEqual(-2, self.car.wheel_angle)

    def test_turn_left(self):
        self.car.start()
        self.car.turn_left()
        self.assertEqual(2, self.car.wheel_angle)   

    def test_speed_up(self):
        self.car.start()
        self.car.speed_up()
        self.assertEqual(30, self.car.velocity)  

    def test_slow_down(self):
        self.car.start()
        self.car.velocity += 40
        self.car.slow_down()
        self.assertEqual(10, self.car.velocity)  

    def test_stop(self):
        self.car.start()
        self.car.velocity += 40
        self.car.stop()
        self.assertEqual(0, self.car.velocity) 

    def test_fuel_check(self):
        self.car.start()
        self.car.fuel_level += 10
        self.assertEqual(True, self.car.car_fuel_flag)

    def test_fuel_fill(self):
        self.car.start()
        self.car.fuel_level = 50
        self.car.fuel_fill()
        self.assertEqual(100, self.car.fuel_level)

    def fuel_check_false(self):
        self.car.start()
        self.car.fuel_level = 0
        self.assertEqual(False, self.car.car_fuel_flag)

    def test_fuel_fill_below_zero(self):
        self.car.start()
        self.car.fuel_level = 0
        self.car.fuel_fill()
        self.assertEqual(100, self.car.fuel_level)

if __name__ == '__main__':
    unittest.main()

    


