from servisable import Servisable

class Car(Servisable):
    def __init__(self, engine, battery, tiers):
        self.engine = engine
        self.battery = battery
        self.tires = tiers

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()