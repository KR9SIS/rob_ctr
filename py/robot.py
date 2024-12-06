import socket

from feedback import FeedbackData, feedback_data_arr
from numpy import frombuffer


class RobotConn:
    """
    Active connection to the robot which acts as an interface for it.
    """

    def __init__(self, dashboard_cmd_stream, motion_cmd_stream):
        self.dashboard_cmd_stream = dashboard_cmd_stream
        self.motion_cmd_stream = motion_cmd_stream

    @classmethod
    def connect(cls):
        """
        Creates a connection to the robot.
        Port 29999 is the settings port used to enable or disable the arm
        Port 30003 is the movement port used to send movement instructions to the arm

        :return RobotConn object with active connection to the two ports
        """
        dashboard_conn = socket.create_connection(("192.168.1.6", 29999))
        motion_conn = socket.create_connection(("192.168.1.6", 30003))
        return cls(dashboard_conn, motion_conn)

    def enable_robot(self):
        """
        Function calling port 29999 to enable robot
        """
        self.dashboard_cmd_stream.sendall(b"EnableRobot()\n")

    def disable_robot(self):
        """
        Function calling port 29999 to disable robot
        """
        self.dashboard_cmd_stream.sendall(b"DisableRobot()\n")

    def set_do(self, index, status):
        """
        Function calling port 2999 to change Digital Output stream
        """
        self.dashboard_cmd_stream.sendall(f"DO({index}, {status})\n".encode())

    def mov_j(self, x, y, z, r):
        """
        Function calling port 30003
        """
        self.motion_cmd_stream.sendall(f"MovJ({x}, {y}, {z}, {r})\n".encode())


class RobotFeedbackConn:
    """
    Class to return the current status of the robot
    """
    def __init__(self, feedback_conn):
        self.feedback_conn = feedback_conn

    @classmethod
    def connect(cls):
        """
        Create connection to port 30004
        """
        feedback_conn = socket.create_connection(("192.168.1.6", 30004))
        return cls(feedback_conn)

    def receive_feedback(self):
        buffer = self.feedback_conn.recv(1440)
        return frombuffer(buffer, dtype=FeedbackData)[0]

    def print_feedback(self, feedback):
        """
        Print out all data from Robot Status with its header
        """
        print("Arm Coordinates", feedback[31][0:4])
        _ = [print(header, data) for header, data in zip(feedback_data_arr, feedback)]
