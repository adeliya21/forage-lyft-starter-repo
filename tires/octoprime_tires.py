from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tire_list : [None]*4):
        self.tire_list = tire_list
    
    def needs_service(self):
        sum = 0
        for tire in self.tire_list:
            sum += tire

        if sum >= 3:
            return True
        return False