import unittest

from datetime import datetime
from car_factory import Car_Factory

''' CALIOPE CAR '''
#@unittest.skip('calliope')
class TestCalliope(unittest.TestCase):
    ''' BATTERY '''
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())

    ''' ENGINE '''
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Car_Factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Car_Factory.create_calliope(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())

''' Glissade '''
#@unittest.skip('glissade')
class TestGlissade(unittest.TestCase):
    ''' BATTERY '''
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())

    ''' ENGINE '''
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Car_Factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Car_Factory.create_glissade(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())

''' PALINDROME '''
#@unittest.skip('palindrome')
class TestPalindrome(unittest.TestCase):
    ''' BATTERY '''
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        warning_light_is_on = False

        car = Car_Factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)
        warning_light_is_on = False

        car = Car_Factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.battery.needs_service())

    ''' ENGINE '''
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        car = Car_Factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        car = Car_Factory.create_palindrome(current_date, last_service_date, warning_light_is_on)
        self.assertFalse(car.engine.needs_service())

''' RORSCHACH '''
#@unittest.skip('rorschach')
class TestRorschach(unittest.TestCase):
    ''' ENGINE '''
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

    ''' BATTERY '''
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60001
        last_service_mileage = 0

        car = Car_Factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 60000
        last_service_mileage = 0

        car = Car_Factory.create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.needs_service())

''' THOVEX '''
#@unittest.skip('hovex')
class TestThovex(unittest.TestCase):
    ''' BATTERY '''
    def test_battery_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)
        current_mileage = 0
        last_service_mileage = 0

        car = Car_Factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.battery.needs_service())
    
    ''' BATTERY '''
    def test_engine_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30001
        last_service_mileage = 0

        car = Car_Factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(car.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = datetime.today().date()
        current_mileage = 30000
        last_service_mileage = 0

        car = Car_Factory.create_thovex(current_date, last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(car.engine.needs_service())


if __name__ == '__main__':
    unittest.main()
