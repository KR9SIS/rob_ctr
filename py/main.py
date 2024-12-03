import argparse

from robot import RobotConn, RobotFeedbackConn


def parse_args():
    parser = argparse.ArgumentParser(description="Cli to control dobot robot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("on", help="Turn on the robot")
    subparsers.add_parser("off", help="Turn off the robot")

    move_parser = subparsers.add_parser("move", help="Move the robot")
    move_parser.add_argument("x", type=float, help="X coordinate")
    move_parser.add_argument("y", type=float, help="Y coordinate")
    move_parser.add_argument("z", type=float, help="Z coordinate")
    move_parser.add_argument("r", type=float, help="R coordinate")

    do_parser = subparsers.add_parser("do", help="Set DO")
    do_parser.add_argument("index", type=int, help="Index")
    do_parser.add_argument("status", type=int, help="Status")

    subparsers.add_parser("feedback", help="Get feedback from the robot")

    return parser.parse_args()


def main():
    args = parse_args()
    robot = RobotConn.connect()

    if args.command == "on":
        robot.enable_robot()
    elif args.command == "off":
        robot.disable_robot()
    elif args.command == "move":
        robot.mov_j(args.x, args.y, args.z, args.r)
    elif args.command == "do":
        robot.set_do(args.index, args.status)
    elif args.command == "feedback":
        feedback = RobotFeedbackConn.connect().receive_feedback()
        print(feedback)


if __name__ == "__main__":
    main()
