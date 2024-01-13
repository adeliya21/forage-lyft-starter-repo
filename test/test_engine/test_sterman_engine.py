import unittest

from engine.sternman_engine import SternmanEngine

#@unittest.skip('sterman engine')
class Test_StermanEngine(unittest.TestCase):
    def test_egine_needs_service_true(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_egine_needs_service_false(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)
        self.assertFalse(engine.needs_service())