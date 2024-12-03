import pickle
import socket


class RobotConn:
    def __init__(self, dashboard_cmd_stream, motion_cmd_stream):
        self.dashboard_cmd_stream = dashboard_cmd_stream
        self.motion_cmd_stream = motion_cmd_stream

    @classmethod
    def connect(cls):
        dashboard_conn = socket.create_connection(("192.168.1.6", 29999))
        motion_conn = socket.create_connection(("192.168.1.6", 30003))
        return cls(dashboard_conn, motion_conn)

    def enable_robot(self):
        self.dashboard_cmd_stream.sendall(b"EnableRobot()\n")

    def disable_robot(self):
        self.dashboard_cmd_stream.sendall(b"DisableRobot()\n")

    def set_do(self, index, status):
        self.dashboard_cmd_stream.sendall(f"DO({index}, {status})\n".encode())

    def mov_j(self, x, y, z, r):
        self.motion_cmd_stream.sendall(f"MovJ({x}, {y}, {z}, {r})\n".encode())


class RobotFeedbackConn:
    def __init__(self, feedback_conn):
        self.feedback_conn = feedback_conn

    @classmethod
    def connect(cls):
        feedback_conn = socket.create_connection(("192.168.1.6", 30004))
        return cls(feedback_conn)

    def receive_feedback(self):
        buffer = self.feedback_conn.recv(1440)
        feedback_data = pickle.loads(buffer)
        return feedback_data
