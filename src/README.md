# DOBOT MG400 Robot Arm Control
## main
This is a script used to send commands to the DOBOT MG400. It can be run with or without arguments, if it is run without then **move_loop** will be called.
### Arguments
#### *move_loop (default)*
  Automatically enables the arm, then enters a loop which repeatedly calls for user input to move the arm.
  The input must be numbers or the following characters
  - 'x', 'y', 'z', and 'r' as numbers
    Moves the arm to the corresponding coordinates of the numbers. Accepts both integers and floating point numbers.
 	***Example:*** `Command: 290 0.0 125.0 0`
	Will call `MovJ(290, 0.0, 125.0, 0`.
	If less than four numbers are input the command will be padded with the previous coordinates for the missing values.

	***Example:*** `Command: 305`

	Will call `MovJ(305, 0.0, 125.0, 0)`.
	While excess values given will only look at the first 4 coordinates.

	***Example:*** `Command: 290 -20.5 90.7 10 20 30 ... 50`
	 Will call `MovJ(290, -20.5, 90.7, 10)`.

	***Error:*** `Command: 1000 -1000 -500 500`
	Will throw a ControllerError, causing the robot to make beeping sound and stop execution. Arm range depends on it's joints but the best way to find your coordinates is to start at the home position (290 0 125 0) where all joints are 90˚ and move the arm in increments from there.

    <img src="/StudioPro/workspace1.png" alt="X & Z axis robot workspace" style="width:40%; height:auto;">
    <img src="/StudioPro/workspace2.png" alt="X & Y axis robot workspace" style="width:40%; height:auto;">
  - 'x', 'y', 'z', or 'r' as characters
    Uses previous value of 'x', 'y', 'z', or 'r'.
	***Example with current coordinates 290, 20.5, 90.7, 10:***
	   `Command: x y 155.5 r`
	   Will call `MovJ(290, 20.5, 155.5, 10)`.
  - 's'
    Outputs the current status of the robot arm.
	***Example:*** `Command: s`
  - 'ce'
    Clears any errors currently being thrown by the robot arm, resets it and readies it for further use.
		***Example:*** `Command: ce`
  - 'home'
	Moves the arm back to the home position 290 0 125 0 where all joints are at a 90°angle.
		***Example:*** `Command: home`
  - 'q'
    Exits the loop, moves the arm back to home position, disables the arm and exits the program.
		***Example:*** `Command: q`
---
#### *on*
  Enable the robot arm, readying it for move commands.
    ***Example:*** `python main.py on`

---
#### *off*
  Disable the robot arm.
    ***Example:*** `python main.py off`

---
#### *move*
  Sends a singular MovJ instruction to the arm.
  Requires that you input 4 numbers 'x', 'y', 'z' and 'r' with it. These numbers can either be floating point numbers or integers.
  ***Example:*** `python main.py move 290.0 0 125 0.0`

  ***Error:*** `Command: 1000 -1000 -500 500`
  Will throw a ControllerError, causing the robot to make beeping sound and stop execution. Arm range depends on it's joints but the best way to find your coordinates is to start at the home position (290 0 125 0) where all joints are 90˚ and move the arm in increments from there.

  <img src="/StudioPro/workspace1.png" alt="X & Z axis robot workspace" style="width:40%; height:auto;"> <img src="/StudioPro/workspace2.png" alt="X & Y axis robot workspace" style="width:40%; height:auto;">

---
#### *status*
  Prints out the current status of the arm.
    ***Example:*** `python main.py status`

---
## robot
This file is a class definition for RobotConn and its methods. Raises TimeoutError if connection cannot be made to MG400.

## rob_status
This file is a definition for a numpy datatype mapping the status bytes given by the robot to their respective values.

