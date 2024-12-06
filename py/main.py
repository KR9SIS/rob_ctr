import argparse

from robot import RobotConn, RobotFeedbackConn


def parse_args():
    """
    Argument parser called by the main function
    """
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

    subparsers.add_parser("move_loop", help="Continously move the robot")

    subparsers.add_parser("feed_loop", help="Continously get feedback from the robot")

    return parser.parse_args()


def get_feedback():
    """
    Gets feedback from MG400 off port 3004 and prints it to std out.
    """
    rfc = RobotFeedbackConn.connect()
    feedback = rfc.receive_feedback()
    rfc.print_feedback(feedback)


def move_loop(robot):
    """
    GUI interface to repeatedly move the arm or access feedback from it.
    :params robot RobotConn
    Asks for four input coordinates to move the arm to.
    If it get's less than that then it fills in with the previous coordinates given.
    Default coordinates are x: 270 and y, z and r: 0
    """
    robot.enable_robot()
    on = True
    x = 270
    y = z = r = 0
    coords: list = [x, y, z, r]
    while on:
        cmd = input(
            "\nPlease input 'x y z r' coordinates\nor 'f' for feedback\nor 'q' to quit\nCommand: "
        ).lower()
        if cmd not in ("q", "f"):
            coords = cmd.split()
            if "x" in coords:
                coords[0] = x
            if "y" in coords:
                coords[1] = y
            if "z" in coords:
                coords[2] = z
            if "r" in coords:
                coords[3] = r

            coords = list(map(int, coords))
            cmd_num = len(coords)
            if cmd_num > 4:
                coords = coords[0:4]
                x, y, z, r = coords

            elif cmd_num < 4:
                match cmd_num:
                    case 0:
                        pass  # Use previous coordinates
                    case 1:
                        x = coords[0]
                    case 2:
                        x, y = coords[0:2]
                    case 3:
                        x, y, z = coords[0:3]
            else:
                x, y, z, r = coords

            print(f"x: {x}, y: {y}, z: {z}, r: {r}")
            # robot.mov_j(x, y, z, r)
        elif cmd == "f":
            get_feedback()
        elif cmd == "q":
            on = False

    robot.disable_robot()


def main():
    """
    Main function to operate the dobot arm
    Call the function with one of the following arguments
    'on' to enable the robot
    'off' to disable the robot
    'move' after enabling to move the robot once
    'do' to set status of digital output port
    'feedback' to get the current feedback about the arm from port 2004
    'move_loop' to activate multiple movements and feedback from the arm
    """
    args = parse_args()
    robot = RobotConn.connect()

    match args.command:
        case "on":
            robot.enable_robot()
        case "off":
            robot.disable_robot()
        case "move":
            robot.mov_j(args.x, args.y, args.z, args.r)
        case "do":
            robot.set_do(args.index, args.status)
        case "feedback":
            get_feedback()
        case "move_loop":
            move_loop(robot)
        case "feed_loop":
            while True:  # Feedback will continue to print until ctr + c is pressed
                get_feedback()


if __name__ == "__main__":
    main()
