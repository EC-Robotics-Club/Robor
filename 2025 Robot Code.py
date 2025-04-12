
# TEAM 12 ROBOT CODE
# #completely self made, trust no cap
# # EXTENDED AND MODIFIED FOR USE BY Byron, Nigel, and Abe
import time
# #air test
# # Device IDs
LMOTOR_ID = "6_7490656656070236256"
RMOTOR_ID = "6_11584292962467012355"

# # Motors
LEFT_MTR = "b"
RIGHT_MTR = "a"
DOOR_MTR = "b"

setupDone = False

# # Controls (change these to your preferences) ------------------@@

# # keyboard / gamepad buttons--
FORWARD = "w"
BACKWARD = "s"
TURN_RIGHT = "d"
TURN_LEFT = "a"
DOOR_RIGHT = "p"
DOOR_LEFT = "o"

def autonomous():
    Robot.set_value(LMOTOR_ID, "pid_enabled_a", False)
    Robot.set_value(RMOTOR_ID, "pid_enabled_a", False)
    Robot.set_value(LMOTOR_ID, "pid_enabled_b", False)
    Robot.set_value(RMOTOR_ID, "pid_enabled_b", False)
    Robot.set_value(LMOTOR_ID, "invert_a", False)
    Robot.set_value(RMOTOR_ID, "invert_a", True)
    Robot.set_value(LMOTOR_ID, "invert_b", False)
    Robot.set_value(RMOTOR_ID, "invert_b", False)
    Robot.set_value(RMOTOR_ID, "velocity_a", 1)
    Robot.set_value(LMOTOR_ID, "velocity_b", 1)
    Robot.set_value(RMOTOR_ID, "velocity_b", 0)
    Robot.set_value(LMOTOR_ID, "velocity_a", 0)

def teleop():
    while(True):
        Robot.set_value(LMOTOR_ID, "pid_enabled_a", True)
        Robot.set_value(RMOTOR_ID, "pid_enabled_a", True)
        Robot.set_value(LMOTOR_ID, "pid_enabled_b", True)
        Robot.set_value(RMOTOR_ID, "pid_enabled_b", True)
        Robot.set_value(LMOTOR_ID, "invert_a", False)
        Robot.set_value(RMOTOR_ID, "invert_a", True)
        Robot.set_value(LMOTOR_ID, "invert_b", False)
        Robot.set_value(RMOTOR_ID, "invert_b", False)
        left = 0
        right = 0
        Robot.set_value(RMOTOR_ID, "velocity_b", 0.0)
        if (Keyboard.get_value(FORWARD)):
            right += 1.0
            left += 1.0
        if (Keyboard.get_value(BACKWARD)):
            left -= 1.0
            right -= 1.0
        if (Keyboard.get_value(TURN_RIGHT)):
            right = -1.0
            left = 1.0
        if (Keyboard.get_value(TURN_LEFT)):
            right = 1.0
            left = -1.0
        if (Keyboard.get_value(DOOR_LEFT)):
            Robot.set_value(RMOTOR_ID, "velocity_b", -1.0)
        if (Keyboard.get_value(DOOR_RIGHT)):
            Robot.set_value(RMOTOR_ID, "velocity_b", 1.0)
        Robot.set_value(LMOTOR_ID, "velocity_b", left)
        Robot.set_value(RMOTOR_ID, "velocity_a", right)