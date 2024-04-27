# TEAM 12 ROBOT CODE
#completely self made, trust no cap
# EXTENDED AND MODIFIED FOR USE BY Byron, Nigel, and Abe

import time

# Motors (writing it out like this so that each motor is clearly related to its designated motor controller)
LEG_MOTOR_ID = "6_13044163168695452367"
ADJACENT_MTR = "a"
OPPOSITE_MTR = "b"
CLAW_SERVO_ID = "yappington"

HYP_MOTOR_ID = "6_7190284582464944900"
HYP_MTR = "a"
ARM_MTR = "b" # uses same motor controller as hyp wheel
CLAW_SERVO = "1"

# ARM_MOTOR_ID = "N/A"
# ARM_MTR = "a"

# O |\ H
#   |_\
#    A

# Controls (change these to your preferences) ------------------@@

# Control scheme: keyboard_tank, keyboard_wasd, gamepad
INPUT_TYPE = "keyboard_wasd"

# keyboard / gamepad buttons--
LEFT_MOTOR_FORWARD = "w"
LEFT_MOTOR_BACKWARD = "q"
RIGHT_MOTOR_FORWARD = "o"
RIGHT_MOTOR_BACKWARD = "p"

FORWARD = "w"
BACKWARD = "s"
TURN_RIGHT = "d"
TURN_LEFT = "a"

STRAFE_LEFT = "o"
STRAFE_RIGHT = "p"

ARM_UP = "q"
ARM_DOWN = "e"


CLAW_OPEN = "k"
CLAW_CLOSE = "l"
# --------------------------------------------------------------@@

def claw_code():
    Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SERVO, 0)

    # target = CLAW_CLOSED_POS
    # is_pressed = False
    
    while True:
        if Keyboard.get_value(CLAW_OPEN):
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SERVO, 0)
        elif Keyboard.get_value(CLAW_CLOSE):
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SERVO, -1)
    
        else:
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SERVO, 0)



def motor_setup():
    Robot.set_value(LEG_MOTOR_ID, "pid_enabled_" + OPPOSITE_MTR, False)
    Robot.set_value(LEG_MOTOR_ID, "pid_enabled_" + ADJACENT_MTR, False)
    Robot.set_value(HYP_MOTOR_ID, "pid_enabled_" + HYP_MTR, False)
    Robot.set_value(HYP_MOTOR_ID, "invert_" + HYP_MTR, True)

def autonomous_setup():
    #Autonomous Not Altered
    print("Autonomous up")
    motor_setup()

def autonomous_main():
    starttime = time.time()
    while time.time() - starttime < 3.65:
        pass
    while time.time() - starttime > 3.65 and time.time() - starttime < 4.15:
        pass
    while time.time() - starttime > 4.15:
        Robot.set_value(LEG_MOTOR_ID, "velocity_" + OPPOSITE_MTR, 0)
        Robot.set_value(LEG_MOTOR_ID, "velocity_" + ADJACENT_MTR, 0)
        Robot.set_value(HYP_MOTOR_ID, "velocity_" + HYP_MTR, 0)

def teleop_setup():
    print("Teleop Mode has started!")
    
    # Start the arm_code() and claw_code() function running simultaneously with teleop_main()
    # Robot.run(arm_code)
    # Robot.run(claw_code)
    
    motor_setup()

# Drive code
def teleop_main():
    armMove = 0
    if Keyboard.get_value(ARM_UP):
        armMove += 1
    if Keyboard.get_value(ARM_DOWN):
        armMove -= 1
    
    Robot.set_value(HYP_MOTOR_ID, "velocity_" + ARM_MTR, armMove)

    if INPUT_TYPE == "keyboard_wasd": 
        turn = 0
        if Keyboard.get_value(TURN_LEFT):
            turn -= 1
        if Keyboard.get_value(TURN_RIGHT):
            turn += 1

        forward = 0
        if Keyboard.get_value(FORWARD):
            forward += 1
        if Keyboard.get_value(BACKWARD):
            forward -= 1

        strafe = 0
        if Keyboard.get_value(STRAFE_LEFT):
            strafe -= 1
        if Keyboard.get_value(STRAFE_RIGHT):
            strafe += 1

        if forward == 0 and strafe == 0:

            Robot.set_value(LEG_MOTOR_ID, "velocity_" + OPPOSITE_MTR, turn)
            Robot.set_value(LEG_MOTOR_ID, "velocity_" + ADJACENT_MTR, turn)
            Robot.set_value(HYP_MOTOR_ID, "velocity_" + HYP_MTR, turn)
                
        if turn == 0 and strafe == 0:
                    
            Robot.set_value(LEG_MOTOR_ID, "velocity_" + OPPOSITE_MTR, forward)
            Robot.set_value(LEG_MOTOR_ID, "velocity_" + ADJACENT_MTR, forward * -1)

        if forward == 0 and turn == 0:

            Robot.set_value(HYP_MOTOR_ID, "velocity_" + HYP_MTR, strafe)
            Robot.set_value(LEG_MOTOR_ID, "velocity_" + ADJACENT_MTR, strafe * -0.5)
            Robot.set_value(LEG_MOTOR_ID, "velocity_" + OPPOSITE_MTR, strafe * -0.5)
            