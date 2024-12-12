import socket
from threading import Lock, Thread

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
        dash_serv_stream,
        motion_serv_stream,
    ):
        self.dashboard_cmd_stream = dashboard_cmd_stream
        self.dash_serv_stream = dash_serv_stream
        self.motion_cmd_stream = motion_cmd_stream
        self.motion_serv_stream = motion_serv_stream
        self.thread_lock = Lock()

    @classmethod
    def connect(cls):
        """
        Creates a connection to the robot.
        Port 29999 is the settings port used to enable or disable the arm
        Port 30003 is the movement port used to send movement instructions to the arm

        :return RobotConn object with active connection to the two ports
        """
        dashboard_conn = socket.create_connection(("192.168.1.6", 29999))
        dash_serv_conn = Thread(
            target=cls.__setup_server, args=(dashboard_conn,), daemon=True
        )
        motion_conn = socket.create_connection(("192.168.1.6", 30003))
        motion_serv_conn = Thread(
            target=cls.__setup_server, args=(motion_conn,), daemon=True
        )

        return cls(dashboard_conn, motion_conn, dash_serv_conn, motion_serv_conn)

    def __s_print(self, *a, **b):
        with self.thread_lock:
            print(*a, **b)

    def __setup_server(self, conn):
        while True:
            data = conn.recv(64).decode("utf-8")
            self.__s_print(data)

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
