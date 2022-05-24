
class control:
    def __init__(self,api):
        self.api =api

    def turn_by_angle_and_speed(self, angle,speed):
        self.api.setSteeringAngle(int(angle))
        self.api.setMotorPower(speed)

    def stop_sign(self):
        self.api.setSteeringAngle(0)
        self.api.setMotorPower(0)

    def work_on_road_change_lane(self):
        pass

    def speed_30(self):
        self.api.setSteeringAngle(0)
        self.api.setMotorPower(30)
