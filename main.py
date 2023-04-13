import matplotlib
#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

motor_turns_arm = Motor(Port.C)
sensor_stops_arm = TouchSensor(Port.S1)
arm_color_sensor = ColorSensor(Port.S2)
arm_elbow_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, [8, 40])
claw_motor = Motor(Port.A)

# Write your program here.
#ev3.speaker.beep()

###################Kalibrering##########
def calibrate():
    claw_motor.run_until_stalled(200,then=Stop.COAST, duty_limit=50)
    claw_motor.reset_angle(0)
    claw_motor.run_target(200,-90)
    
    arm_elbow_motor.run_until_stalled(60, then=Stop.COAST,duty_limit=30)
    arm_elbow_motor.reset_angle(0)
    arm_elbow_motor.run_until_stalled(-60, then=Stop.COAST,duty_limit=30)
    
    while not sensor_stops_arm.pressed():
        motor_turns_arm.run_time(40, 350, then=Stop.HOLD,wait = True)
    

###################Moves arm up#########
def arm_up():
    arm_elbow_motor.run_time(50, 1800, then=Stop.HOLD,wait = True)

def arm_middel_up():
    arm_elbow_motor.run_time(45.7, 1200, then=Stop.HOLD,wait = True)
    arm_elbow_motor.hold()

##################Moves arm down########
def arm_down():
    arm_elbow_motor.run_time(-50, 1800, then=Stop.HOLD,wait = True)


################Color Sensor#############
def color_sense():
    runing = True
    while runing:
        if arm_color_sensor.color() == Color.BLUE:
            ev3.speaker.say("I found a blue brick")
            blue_brick()
            return "blue"
        elif arm_color_sensor.color() == Color.RED:
            ev3.speaker.say("I found a red brick")
            red_brick()
            return "red"    
        else:
            ev3.speaker.say("Nothing found")
            return None

def color_sense2():
    if arm_color_sensor.color() == Color.BLUE:
        ev3.speaker.say("I found a blue brick")
        blue_brick()
        return "blue"
    elif arm_color_sensor.color() == Color.RED:
        ev3.speaker.say("I found a red brick")
        red_brick()
        return "red"    
    else:
        ev3.speaker.say("Nothing found")
        nothing()
        return None
##########Found Brick###################
def blue_brick():
    motor_turns_arm.run_time(-100,3400,then=Stop.HOLD,wait = True)
    arm_elbow_motor.run_time(-45.7, 1200, then=Stop.HOLD,wait = True)

    claw_motor.run_target(200,-90)

    arm_elbow_motor.run_time(45.7, 1200, then=Stop.HOLD,wait = True)
    motor_turns_arm.run_time(100,3400,then=Stop.HOLD,wait = True)


def red_brick():
    motor_turns_arm.run_time(-100,6000,then=Stop.HOLD,wait = True)
    arm_elbow_motor.run_time(-45.7, 1200, then=Stop.HOLD,wait = True)

    claw_motor.run_target(200,-90)

    arm_elbow_motor.run_time(45.7, 1200, then=Stop.HOLD,wait = True)
    motor_turns_arm.run_time(100,6000,then=Stop.HOLD,wait = True)

def nothing():
    arm_elbow_motor.run_time(-45.7, 1200, then=Stop.HOLD,wait = True)
    claw_motor.run_target(200,-90)
    grab()

########ta up###########
def grab():
    claw_motor.run_until_stalled(300,then=Stop.HOLD, duty_limit=50)
    claw_motor.hold()
    arm_middel_up()


def main():
    calibrate()
    #arm_up()
    #grab()
    #run=True
    #while run:
    #    color_sense2()



main()
