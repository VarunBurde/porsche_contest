import time
from CarAPI import CarApi
from helper.obstacle_avoidance import distance_sensor
from helper.sign_detection import sign_net
from helper.actuator_control import control
from helper.lane_detection import lane_detect

api = CarApi()
api.startContDistMeas()

if __name__ == '__main__':

    colision_chk = distance_sensor(api)
    drive_obj = control(api)
    sign_obj = sign_net()
    lane_obj =  lane_detect()

    ### control loop
    while True:
        img = None
        collision = colision_chk.check_collision()
        sign = sign_obj.sign(img)
        angle, speed = lane_obj.find_angle_speed(image=)

        if not collision and not sign:
            drive_obj.turn_by_angle_and_speed(angle, speed)

        if sign == 'stop':
            drive_obj.stop_sign()

        if sign == 'speed30':
            drive_obj.speed_30()

        if sign == 'work_on_road':
            drive_obj.work_on_road_change_lane()
