import unittest

from tires.carrigan_tires import CarriganTires

class Test_CarriganTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_list = [0, 0, 0, 0.9]
        tires = CarriganTires(tire_list)
        self.assertTrue(tires.needs_service())
    
    def test_needs_service_false(self):
        tire_list = [0, 0, 0, 0.8]
        tires = CarriganTires(tire_list)
        self.assertFalse(tires.needs_service())