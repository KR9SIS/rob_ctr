# Connecting to the robot arm
More info can be found within "StudioPro/MG400 QUICKSTART GUIDE.pdf"

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
If needed then you can stop the transmission by pressing `CTRL + c`

## Making the connection
The robot accepts TCP/IP requests to talk to it.
You can send them with for example Python using its socket module.
***Example codeblock:***
```
import socket
s_setting = socket.socket().connect("192.168.1.6", "29999")
s_move = socket.socket().connect("192.168.1.6", "30003")

s_setting.sendall(b"enablerobot()")

s_move.sendall(b"movej(350, 65, 45, 20)")
s_move.sendall(b"movej(290, 0, 125, 0)") # MG400 home position

s_setting.sendall(b"disablerobot()")

s_setting.close()
s_move.close()
```
# Operating the robot arm
"src/main.py" is a script used to control the robot arm.
If however you need more specific information or requests then all manuals for the Dobot MG400 can be found in "StudioPro/"
## TCP IP Interface Docs
More information about specific TCP/IP commands for the robot can be found in *"StudioPro/TCP_IP Remote Control Interface Guide"*
#### Small Typo in feedback table
The TCP Interface guide has a typo in the feedback table
It says that the N/A which is between SixForceOnline and MActual is 1 char, and supposedly 82 bytes.
It also says that the N/A which is at the bottom of the table is 1 char and 24 bytes.
In *"src/rob_status"* the first one was padded with 41 int16 to fill up the 82 bytes and the second one was padded with 12 int16 to fill up the 24 bytes.
