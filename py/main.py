import argparse
from time import sleep

from robot import RobotConn, RobotStatusConn


def parse_args():
    """
    Argument parser called by the main function
    """
    parser = argparse.ArgumentParser(description="Cli to control dobot robot")
    subparsers = parser.add_subparsers(dest="command")
    subparsers.default = "move_loop"

    subparsers.add_parser("on", help="Turn on the robot")
    subparsers.add_parser("off", help="Turn off the robot")

    move_parser = subparsers.add_parser("move", help="Move the robot")
    move_parser.add_argument("x", type=float, help="X coordinate")
    move_parser.add_argument("y", type=float, help="Y coordinate")
    move_parser.add_argument("z", type=float, help="Z coordinate")
    move_parser.add_argument("r", type=float, help="R coordinate")

    do_parser = subparsers.add_parser("do", help="Set Digital Output")
    do_parser.add_argument("index", type=int, help="Index")
    do_parser.add_argument("status", type=int, help="Status")

    subparsers.add_parser("status", help="Get robot status")

    subparsers.add_parser("move_loop", help="Continously move the robot")

    subparsers.add_parser("feed_loop", help="Continously get feedback from the robot")

    return parser.parse_args()


def get_rob_status():
    """
    Gets feedback from MG400 off port 30004 and prints it to std out.
    """
    rfc = RobotStatusConn.connect()
    status = rfc.receive_rob_status()
    rfc.print_status(status)


def move_loop(robot):
    """
    GUI interface to repeatedly move the arm or access feedback from it.
    :params robot RobotConn
    Asks for four input coordinates to move the arm to.
    If it get's less than that then it fills in with the previous coordinates given.
    Default coordinates are x: 270 and y, z and r: 0
    """

    def match_s_ce_q(cmd):
        """
        :return tuple[matched, continue_loop]
        """
        match cmd:
            case "q":
                return (True, False)
            case "s":
                with robot.thread_lock:
                    get_rob_status()
                    return (True, True)
            case "ce":
                robot.clear_error()
                return (True, True)

        return (False, True)

    def parse_coords(coords, x, y, z, r):

        if "x" in coords:
            coords[0] = x
        if "y" in coords:
            coords[1] = y
        if "z" in coords:
            coords[2] = z
        if "r" in coords:
            coords[3] = r

        try:
            coords = list(map(int, coords))

            coord_num = len(coords)
            if coord_num > 4:
                coords = coords[0:4]
                x, y, z, r = coords

            elif coord_num < 4:
                match coord_num:
                    case 0:
                        print("No coordinates, staying in place")
                        return (x, y, z, r)
                    case 1:
                        x = coords[0]
                    case 2:
                        x, y = coords[0:2]
                    case 3:
                        x, y, z = coords[0:3]
            else:
                x, y, z, r = coords

            # print(f"x: {x}, y: {y}, z: {z}, r: {r}")
            robot.mov_j(x, y, z, r)
            return (x, y, z, r)

        except ValueError:
            print(
                "Only input numbers or the characters:\n'x', 'y', 'z', 'r', 's', 'ce', or 'q'"
            )
            return (x, y, z, r)

    robot.enable_robot()
    on = True
    x = 270
    y = z = r = 0
    while on:
        sleep(0.2)
        with robot.thread_lock:
            cmd = input(
                "\nPlease input 'x y z r' coordinates\nor 's' for status\nor 'ce' to clear error\nor 'q' to quit\nCommand: "
            ).lower()
            print()

        matched, continue_loop = match_s_ce_q(cmd)
        if not continue_loop:
            on = False
        elif not matched:
            x, y, z, r = parse_coords(cmd.split(), x, y, z, r)

    robot.disable_robot()


def main():
    """
    Main function to operate the dobot arm
    Call the function with one of the following arguments
    'on' to enable the robot
    'off' to disable the robot
    'move' after enabling to move the robot once
    'do' to set status of digital output port
    'status' to get the current status about the arm from port 30004
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
        case "status":
            with robot.thread_lock:
                get_rob_status()
        case "move_loop":
            move_loop(robot)


if __name__ == "__main__":
    main()
