from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 0, -10, 0)
sleep(1)
me.send_rc_control(10, 0, 0, 0)
sleep(.5)
me.send_rc_control(0, 0, 10, 0)
me.land()