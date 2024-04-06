ARM_SPD_UP = 0.175
ARM_SPD_DOWN = 0.05
SCOOP_SPD = 0.07
MAX_ARM_HEIGHT = 260
            
# Arm positions 
# (NOT TESTED! You need to find positions that work based on your arm and your reference encoder value)
ARM_UP_POS = 0
ARM_DOWN_POS = -200
            
# Motor Inversions (need to specify / change depending on your control scheme)
LEFT_MTR_INVERT = False
RIGHT_MTR_INVERT = True
            
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
        if current_pos < arm_target_pos:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 1.0)
        elif current_pos > arm_target_pos:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, -1.0)
        else:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 0.0)

CLAW_TOGGLE = "SPACE"
CLAW_OPEN = "c"
CLAW_CLOSE = "v"

# Difference to claw close(bigger is larger gap)

def claw_code():
    Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, 0)

    # target = CLAW_CLOSED_POS
    is_pressed = False
    
    while True:
        if Keyboard.get_value(CLAW_OPEN):
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, 0)
        elif Keyboard.get_value(CLAW_CLOSE):
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, -1)
    
        else:
            Robot.set_value(CLAW_SERVO_ID, "servo" + CLAW_SRV, 0)

def teleop_main():
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