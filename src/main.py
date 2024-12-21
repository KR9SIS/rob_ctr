"""
module to move a dobot MG400
import and run main after setting up connection to get started
"""

import argparse
from time import sleep

from robot import RobotConn


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

    subparsers.add_parser("status", help="Get robot status")

    return parser.parse_args()


def move_loop(robot):
    """
    GUI interface to repeatedly move the arm or access feedback from it.
    :params robot RobotConn
    Asks for four input coordinates to move the arm to.
    If it get's less than that then it fills in with the previous coordinates given.
    Default coordinates are x: 270 and y, z and r: 0
    """

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
            coords = list(map(float, coords))

            coord_num = len(coords)
            if coord_num > 4:
                coords = coords[0:4]
                x, y, z, r = coords

            elif coord_num < 4:
                match coord_num:
                    case 1:
                        x = coords[0]
                    case 2:
                        x, y = coords[0:2]
                    case 3:
                        x, y, z = coords[0:3]
            else:
                x, y, z, r = coords

            robot.mov_j(x, y, z, r)
            return (x, y, z, r)

        except ValueError:
            print(
                "Only input numbers or the characters:\n'x', 'y', 'z', 'r', 's', 'ce', or 'q'"
            )
            return (x, y, z, r)

    robot.enable_robot()
    on = True
    # Home position
    x = 290
    y = 0
    z = 125
    r = 0

    while on:
        sleep(0.2)
        with robot.thread_lock:
            cmd = input(
                "\nPlease input 'x y z r' coordinates\nor 's' for status\nor 'ce' to clear error\nor 'home' for home position\nor 'q' to quit\nCommand: "
            ).lower()
            print()

        match cmd:
            case "":
                print("No coordinates, staying in place")

            case "q":
                on = False

            case "s":
                with robot.thread_lock:
                    robot.get_rob_status()

            case "ce":
                robot.clear_error()

            case "home":
                robot.mov_j(290, 0, 125, 0)

            case _:
                x, y, z, r = parse_coords(cmd.split(), x, y, z, r)

    robot.mov_j(290, 0, 125, 0)
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
    try:
        robot = RobotConn()
    except TimeoutError:
        print("Connection Failed: TimeoutError")
        return

    match args.command:
        case "on":
            robot.enable_robot()
        case "off":
            robot.disable_robot()
        case "move":
            robot.mov_j(args.x, args.y, args.z, args.r)
        case "status":
            with robot.thread_lock:
                robot.get_rob_status()
        case "move_loop":
            move_loop(robot)


if __name__ == "__main__":
    main()
