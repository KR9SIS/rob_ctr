import socket
from threading import Lock, Thread
from time import sleep

from numpy import frombuffer

from rob_status import RobStatusData, status_data_arr


class RobotConn:
    """
    Active connection to the robot which acts as an interface for it.
    """

    def __init__(
        self,
        dashboard_cmd_stream,
        motion_cmd_stream,
    ):
        self.thread_lock = Lock()

        self.dashboard_cmd_stream = dashboard_cmd_stream
        self.dashboard_feed_thread = Thread(
            target=self.__rob_feed_server,
            args=(self.dashboard_cmd_stream,),
            daemon=True,
        )
        self.dashboard_feed_thread.start()

        self.motion_cmd_stream = motion_cmd_stream
        self.motion_feed_thread = Thread(
            target=self.__rob_feed_server,
            args=(self.motion_cmd_stream,),
            daemon=True,
        )
        self.motion_feed_thread.start()

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

    def __rob_feed_server(self, conn):
        """
        Read the response from the robot after sending a command.
        """
        while True:
            try:
                response = conn.recv(1024).decode("utf-8")
                with self.thread_lock:
                    print("Robot response:\n", response)
                sleep(1)
            except socket.error as e:
                with self.thread_lock:
                    print("Error reading response:", e)
                sleep(1)

    def enable_robot(self):
        """
        Function calling port 29999 to enable robot
        """
        self.dashboard_cmd_stream.sendall(b"EnableRobot()\n")
        sleep(1)

    def disable_robot(self):
        """
        Function calling port 29999 to disable robot
        """
        self.dashboard_cmd_stream.sendall(b"DisableRobot()\n")
        sleep(1)

    def set_do(self, index, status):
        """
        Function calling port 2999 to change Digital Output stream
        """
        self.dashboard_cmd_stream.sendall(f"DO({index}, {status})\n".encode())

    def clear_error(self):
        """
        Function to clear an error and reset the robot.
        """
        self.dashboard_cmd_stream.sendall("ClearError()".encode())
        self.disable_robot()
        self.enable_robot()

    def mov_j(self, x, y, z, r):
        """
        Function calling port 30003
        """
        self.motion_cmd_stream.sendall(f"MovJ({x}, {y}, {z}, {r})\n".encode())


class RobotStatusConn:
    """
    Class to return the current status of the robot
    """

    def __init__(self, status_conn):
        self.status_conn = status_conn

    @classmethod
    def connect(cls):
        """
        Create connection to port 30004
        """
        feedback_conn = socket.create_connection(("192.168.1.6", 30004))
        return cls(feedback_conn)

    def receive_rob_status(self):
        """
        Use RobStatusData type to map robot status to stdout
        """
        buffer = self.status_conn.recv(1440)
        return frombuffer(buffer, dtype=RobStatusData)[0]

    def print_status(self, status):
        """
        Print out all data from Robot Status with its header
        """
        print("Arm Coordinates", status[31][0:4])
        _ = [print(header, data) for header, data in zip(status_data_arr, status)]
