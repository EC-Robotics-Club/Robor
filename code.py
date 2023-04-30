# TEAM 12 ROBOT CODE
#completely self made, trust no cap
# EXTENDED AND MODIFIED FOR USE BY AJITH AND DANIEL
import time

# Device IDs
MOTOR_ID = "6_13086570018056326489"
ARM_MOTOR_ID = "6_250532270729745898"
CLAW_SERVO_ID = "4_161219043144571378"

# Motors
LEFT_MTR = "a"
RIGHT_MTR = "b"
ARM_MTR = "a"
CLAW_SRV = "0"

# Controls (change these to your preferences) ------------------@@

# Control scheme: keyboard_tank, keyboard_wasd, gamepad
INPUT_TYPE = "keyboard_wasd"

# --------------------------------------------------------------@@



# keyboard / gamepad buttons--
LEFT_MOTOR_FORWARD = "w"
LEFT_MOTOR_BACKWARD = "q"
RIGHT_MOTOR_FORWARD = "o"
RIGHT_MOTOR_BACKWARD = "p"

FORWARD = "w"
BACKWARD = "s"
TURN_RIGHT = "a"
TURN_LEFT = "d"

ARM_UP = "q"
ARM_DOWN = "e"
ARM_STILL = "0"
#--

# CLAW_TOGGLE = "SPACE"
CLAW_OPEN = "c"
CLAW_CLOSE = "v"
#--

# # Difference to claw close(bigger is larger gap)

# Arm positions 
# (NOT TESTED! You need to find positions that work based on your arm and your reference encoder value)
ARM_UP_POS = 0
ARM_DOWN_POS = -200

# Motor Inversions (need to specify / change depending on your control scheme)
LEFT_MTR_INVERT = False
RIGHT_MTR_INVERT = True

# Misc
ARM_SPD_UP = 0.175
ARM_SPD_DOWN = 0.05
SCOOP_SPD = 0.07

MAX_ARM_HEIGHT = 260



def claw_code():
    Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, 0)

    # target = CLAW_CLOSED_POS
    is_pressed = False
    
    while True:
        if Keyboard.get_value(CLAW_OPEN):
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, 0)
        elif Keyboard.get_value(CLAW_CLOSE):
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, -1)
    
        # else:
            # Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, 0)
        

def arm_code():
    arm_target_pos = ARM_DOWN_POS
    while True:
        # Get the current target position of the arm (Keyboard)
        if Keyboard.get_value(ARM_DOWN):
            arm_target_pos = ARM_DOWN_POS
        elif Keyboard.get_value(ARM_UP):
            arm_target_pos = ARM_UP_POS

        current_pos = Robot.get_value(ARM_MOTOR_ID, "enc_" + ARM_MTR) # Retrieves current position of the arm motor

        # Sets motor going in the correct direction based on whether the arm is on one side or the other side of the target position
        # if current_pos < arm_target_pos:
        #     Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 1.0)
        # elif current_pos > arm_target_pos:
        #     Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, -1.0)
        # else:
        #     Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 0.0)
            
        
        # Improved? Arm Movement Code :)
        if Keyboard.get_value(ARM_UP):
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 0.1)
        elif Keyboard.get_value(ARM_DOWN):
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, -0.1)
        else:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 0.0)

def autonomous_setup():
    print("Autonomous up")
    Robot.set_value(MOTOR_ID, "pid_enabled_" + LEFT_MTR, False)
    Robot.set_value(MOTOR_ID, "pid_enabled_" + RIGHT_MTR, False)
    Robot.set_value(MOTOR_ID, "invert_a", True)

def autonomous_main():
    starttime = time.time()
    while time.time() - starttime < 3.65:
        Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 0.80)
        Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 0.67)
    while time.time() - starttime > 3.65 and time.time() - starttime < 4.15:
        Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 0)
        Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 1)
    while time.time() - starttime > 4.15:
        Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 0)
        Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 0)

def teleop_setup():
    print("Teleop Mode has started!")
    
    # Start the arm_code() and claw_code() function running simultaneously with teleop_main()
    Robot.run(arm_code)
    Robot.run(claw_code)
    
    Robot.set_value(MOTOR_ID, "pid_enabled_" + LEFT_MTR, False)
    Robot.set_value(MOTOR_ID, "pid_enabled_" + RIGHT_MTR, False)
    Robot.set_value(MOTOR_ID, "invert_a", True)

def teleop_main():
    # Drive code
    
    
    
    # Keyboard Controls -------------------------------------------------------
    
    if INPUT_TYPE == "keyboard_tank":
        left = 0
        right = 0
        if (Keyboard.get_value(LEFT_MOTOR_FORWARD)):
            left += 1.0
        if (Keyboard.get_value(LEFT_MOTOR_BACKWARD)):
            left -= 1.0
        if (Keyboard.get_value(RIGHT_MOTOR_FORWARD)):
            right += 1.0
        if (Keyboard.get_value(RIGHT_MOTOR_BACKWARD)):
            right -= 1.0

        Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, left)
        Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, right)
    
    elif INPUT_TYPE == "keyboard_wasd": 
        if Keyboard.get_value(TURN_LEFT):
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, -1)
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 1)
                
        if Keyboard.get_value(TURN_RIGHT):
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 1)
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, -1)
                
        if not (Keyboard.get_value(TURN_RIGHT) or Keyboard.get_value(TURN_LEFT)):
                
            forward = 0
            if Keyboard.get_value(FORWARD):
                forward += 1
            if Keyboard.get_value(BACKWARD):
                forward -= 1
                    
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, forward)
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, forward)