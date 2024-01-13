import unittest

from tires.octoprime_tires import OctoprimeTires

class Test_OctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        tire_list = [1, 2, 0, 0]
        tires = OctoprimeTires(tire_list)
        self.assertTrue(tires.needs_service())
    
    def test_needs_service_false(self):
        tire_list = [0, 0, 0, 0]
        tires = OctoprimeTires(tire_list)
        self.assertFalse(tires.needs_service())