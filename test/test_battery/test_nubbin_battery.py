import unittest 

from battery.nubbin_battery import NubbinBattery
from datetime import date

#@unittest.skip('nubbin battery')
class Test_NubbinBattery(unittest.TestCase):
    def test_battery_needs_service_true(self):
        current_date = date.today()
        last_service_date = current_date.replace(year = current_date.year - 5)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_needs_service_false(self):
        current_date = date.today()
        last_service_date = current_date.replace(year = current_date.year - 3)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())