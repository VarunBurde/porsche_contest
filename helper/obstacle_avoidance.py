
class distance_sensor:
    def __init__(self,api):
        self.api = api
        self.distance = None

    def check_collision(self):
        distance = self.api.getLastDistance()
        if float(distance)< 25.0:
            print(" stopping car")
            return True