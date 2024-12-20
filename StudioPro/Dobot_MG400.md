# Connecting to the robot arm
More info can be found within MG400 QUICKSTART GUIDE.pdf

## Static ethernet cable ip address
Set the ip address of your cable to 192.168.1.x where x is between 1 and 255, but not 6. 

## Arm IP
MG400: 192.168.1.6

## Ports
Setting: 29999
Motion: 30003
RealTimeFeedback: 30004
Summary: 30005
Configurable: 30006

## Checking your connection
To make sure you're properly connected to the robot, you can go to a terminal and write:
`ping 192.168.1.6`
To then stop the transmission you can press CTRL + c

## Making the connection
The robot accepts TCP/IP requests to talk to it.
You can send them with for example Python using its socket module.
Example codeblock:
```
import socket
s = socket.socket()
s.connect("192.168.1.6", "29999")
s.sendall(b"enablerobot()")
s.sendall(b"movej(350, 65, 45, 20)")
s.sendall(b"movej(270, 0, 0, 0)") # Nice default position
s.sendall(b"disablerobot()")
s.close()
```
# Operating the robot arm
## Moving the arm
To find what range the arm operates in check the feedback and only move it a little
Good starting point:
X: 270
Y: 0
Z: 0
R: 0

To operate the arm, run main.py with the argument "move_loop" and send in coordinates for the arm to move to.

Motion Range
J1: +-160˚
J2: -25˚ ~ 85˚
J3: -25˚ ~ 105˚
J4: +- 360˚


# TCP IP Interface Docs
More information about specific commands for the robot can be found in the TCP_IP Remote Control Interface Guide
The TCP Interface guide has a typo in the feedback table
It says that the N/A which is between SixForceOnline and MActual is 1 char, and supposedly 82 bytes.
It also says that the N/A which is at the bottom of the table is 1 char and 24 bytes.

I replaced the first one with 41 int16 to fill up the 82 bytes
And I replaced the second one 12 int16 to fill up the 24 bytes
