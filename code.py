# NOTE FROM PIE STAFF
# This code has not been tested thoroughly on robots; it is meant to be guidance to help improve
# the code you currently have. It will be tested throughout the week and will be available for you
# to use during final competition if you are unable to get working code on your testing day.
# (And yes, it is intentionally hard to use....)

# Device IDs
MOTOR_ID = "6_3209926418129020503"
ARM_MOTOR_ID = "6_11972001198871247580"
ARM_SERVO_ID = "4_1528355177064943655"
LINE_FOLLOWER_ID = "2_3"

# Motors
LEFT_MTR = "a"
RIGHT_MTR = "b"
ARM_MTR = "a"
LEFT_SVO = "0"
RIGHT_SVO = "1"

# Controls (change these to your preferences)

# Control scheme: keyboard, gamepad, gamepad_experimental
INPUT_TYPE = "keyboard"

LEFT_MOTOR_FORWARD = "q"
LEFT_MOTOR_BACKWARD = "w"
RIGHT_MOTOR_FORWARD = "p"
RIGHT_MOTOR_BACKWARD = "o"

ARM_UP = "d"
ARM_DOWN = "k"

CLAW_OPEN = "i"

# Difference to claw close(bigger is larger gap)
CLAW_GIVE = 0.1

# Arm positions 
# (NOT TESTED! You need to find positions that work based on your arm and your reference encoder value)
ARM_UP_POS = 0
ARM_DOWN_POS = -200

# Motor Inversions (need to specify / change depending on your control scheme)
LEFT_MTR_INVERT = False
RIGHT_MTR_INVERT = True

# Misc
ARM_SPD_UP = 0.35
ARM_SPD_DOWN = 0.2
SCOOP_SPD = 0.07

MAX_ARM_HEIGHT = 260


def autonomous_setup():
    Robot.set_value(MOTOR_ID, "pid_enabled_" + LEFT_MTR, False)
    Robot.set_value(MOTOR_ID, "pid_enabled_" + RIGHT_MTR, False)
    
    
def autonomous_main():
    if Robot.get_value(ARM_MOTOR_ID, "enc_a") < 270:
        Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_UP * 1.0)
    Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, -1.0)
    Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, -1.0)


def arm_code():
    arm_target_pos = ARM_DOWN_POS
    while True:
        # Get the current target position of the arm (Keyboard)
        if Keyboard.get_value(ARM_DOWN):
            arm_target_pos = ARM_DOWN_POS
        elif Keyboard.get_value(ARM_UP):
            arm_target_pos = ARM_UP_POS
            
        # Get the current target position of the arm (Xbox Controller)
        #if Gamepad.get_value("l_trigger") == 1:
        #    arm_target_pos = ARM_DOWN_POS
        #elif Gamepad.get_value("r_trigger") == 1:
        #    arm_target_pos = ARM_UP_POS

        # Drive the arm motor to go to the target position USING ENCODERS (think hard about how you can use this to your advantage!)
        # Ask PiE staff what these do and refer to the student API!
        #current_pos = Robot.get_value(ARM_MOTOR_ID, "enc_" + ARM_MTR) # Retrieves current position of the arm motor

        # Sets motor going in the correct direction based on whether the arm is on one side or the other side of the target position
        if current_pos < arm_target_pos:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPEED)
        elif current_pos > arm_target_pos:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPEED * -1.0)
        else:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, 0.0)
            
        
        # Improved? Arm Movement Code
        if Keyboard.get_value(ARM_UP):
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPEED * 1.0)
        elif Keyboard.get_value(ARM_DOWN):
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPEED * -1.0)

def teleop_setup():
    print("Teleop Mode has started!")
    # Start the arm_code() function running simultaneously with teleop_main()
    # Robot.run(arm_code)
    # arm_target_pos = ARM_DOWN_POS
    Robot.set_value(MOTOR_ID, "pid_enabled_" + LEFT_MTR, False)
    Robot.set_value(MOTOR_ID, "pid_enabled_" + RIGHT_MTR, False)
    # Robot.set_value(ARM_MOTOR_ID, "pid_enabled_" + ARM_MTR, False)
    #TILT = 1.0
    
    pass

def teleop_main():
    # Drive code
    
    # Keyboard Controls -------------------------------------------------------
    
    if INPUT_TYPE == "keyboard":
        # Left Motor Movement
        if Keyboard.get_value(LEFT_MOTOR_FORWARD):
         Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 1.0)
        elif Keyboard.get_value(LEFT_MOTOR_BACKWARD):
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, -1.0)
        else:
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 0.0)
    
        # Right Motor Movement
        if Keyboard.get_value(RIGHT_MOTOR_FORWARD):
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 1.0)
        elif Keyboard.get_value(RIGHT_MOTOR_BACKWARD):
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, -1.0)
        else:
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 0.0)
            
        
        #Arm Motor Movement
        if Keyboard.get_value(ARM_UP) and Robot.get_value(ARM_MOTOR_ID, "enc_a") < 270:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_UP * 1.0)
        elif Keyboard.get_value(ARM_DOWN):
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_DOWN * -1.0)
        else:
            # Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_UP * 0.0)
            pass
            
        # Arm Tilting
        # TILT = Robot.get_value(ARM_SERVO_ID, "servo" + LEFT_SVO)

        if Keyboard.get_value(CLAW_OPEN):
            Robot.set_value(ARM_SERVO_ID, "servo" + LEFT_SVO, 0)
            Robot.set_value(ARM_SERVO_ID, "servo" + RIGHT_SVO, 0)
        elif Keyboard.get_value("f"):
            Robot.set_value(ARM_SERVO_ID, "servo" + LEFT_SVO, -1)
            Robot.set_value(ARM_SERVO_ID, "servo" + RIGHT_SVO, 1)
        else:
            # Robot.set_value(ARM_SERVO_ID, "servo" + LEFT_SVO, 1 - CLAW_GIVE)
            # Robot.set_value(ARM_SERVO_ID, "servo" + RIGHT_SVO, -(1 - CLAW_GIVE))
            pass            
        
    # Gamepad Controls -------------------------------------------------------
    
    elif INPUT_TYPE == "gamepad":
        #Left Motor Movement
        if Gamepad.get_value("joystick_left_y") <= -0.5:
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 1.0)
        elif Gamepad.get_value("joystick_left_y") >= 0.5:
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, -1.0)
        else:
            Robot.set_value(MOTOR_ID, "velocity_" + LEFT_MTR, 0.0)
            
        #Right Motor Movement
        if Gamepad.get_value("joystick_right_y") <= -0.5:
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 1.0)
        elif Gamepad.get_value("joystick_right_y") >= 0.5:
            Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, -1.0)
        else:
          Robot.set_value(MOTOR_ID, "velocity_" + RIGHT_MTR, 0.0)
        
        #Arm Motor Movement
        if Gamepad.get_value("l_trigger") != 0:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_UP * 1.0)
        elif Gamepad.get_value("r_trigger") != 0:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_DOWN * -1.0)
        else:
            Robot.set_value(ARM_MOTOR_ID, "velocity_" + ARM_MTR, ARM_SPD_UP * 0.0)
        
        #Arm Tilting
        TILT = Robot.get_value(ARM_SERVO_ID, "servo" + LEFT_SVO)
        if Gamepad.get_value("l_bumper") == 1:
            TILT -= SCOOP_SPD
            Robot.set_value(ARM_SERVO_ID, "servo" + LEFT_SVO, -TILT)
            Robot.set_value(ARM_SERVO_ID, "servo" + RIGHT_SVO, TILT)
        elif Gamepad.get_value("r_bumper") == 1:
            TILT += SCOOP_SPD
            Robot.set_value(ARM_SERVO_ID, "servo" + LEFT_SVO, -TILT)
            Robot.set_value(ARM_SERVO_ID, "servo" + RIGHT_SVO, TILT)