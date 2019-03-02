import re


class Pacman:
    def __init__(self):
        self.face_direction = ''
        self.x_coord = None
        self.y_coord = None

    # Place Pacman on the grid with x,y coords and a direction to face in
    def place(self, X, Y, F):
        directions = ["NORTH", "SOUTH", "EAST", "WEST"]
        if 0 <= int(X) <= 4 and 0 <= int(Y) <= 4 and F in directions:
            self.x_coord = int(X)
            self.y_coord = int(Y)
            self.face_direction = F
        else:
            print("The coordinates or direction given are invalid.")

    # Move 1 unit in the direction Pacman is facing, provided it is on the 5x5 grid
    def move(self):
        if self.face_direction == "NORTH":
            if self.y_coord < 4:
                self.y_coord += 1
            else:
                print("Pacman cannot move any further north.")

        if self.face_direction == "SOUTH":
            if self.y_coord > 0:
                self.y_coord -= 1
            else:
                print("Pacman cannot move any further south.")

        if self.face_direction == "EAST":
            if self.x_coord < 4:
                self.x_coord += 1
            else:
                print("Pacman cannot move any further east.")

        if self.face_direction == "WEST":
            if self.x_coord > 0:
                self.x_coord -= 1
            else:
                print("Pacman cannot move any further west.")

    # Rotate 90 degrees to the left
    def left(self):
        if self.face_direction == "NORTH":
            self.face_direction = "WEST"
        elif self.face_direction == "SOUTH":
            self.face_direction = "EAST"
        elif self.face_direction == "EAST":
            self.face_direction = "NORTH"
        elif self.face_direction == "WEST":
            self.face_direction = "SOUTH"

    # rotate 90 degrees to the right
    def right(self):
        if self.face_direction == "NORTH":
            self.face_direction = "EAST"
        elif self.face_direction == "SOUTH":
            self.face_direction = "WEST"
        elif self.face_direction == "EAST":
            self.face_direction = "SOUTH"
        elif self.face_direction == "WEST":
            self.face_direction = "NORTH"

    # get Pacman's current x and y coordinates as well as his current facing direction
    def report(self):
        print("Current coordinates: ({0},{1}) {2}".format(self.x_coord, self.y_coord, self.face_direction))


def main():
    pacman = Pacman()
    with open("commands", "r") as infile:
        for line in infile:
            # look for first valid PLACE command
            if line.startswith("PLACE"):
                args = re.split('\s|,', line)  # split line by space and comma
                pacman.place(args[1], args[2], args[3])
                # once PLACE command found then run all other commands found
                for command in infile:
                    if command.startswith("MOVE"):
                        pacman.move()
                    elif command.startswith("LEFT"):
                        pacman.left()
                    elif command.startswith("RIGHT"):
                        pacman.right()
                    elif command.startswith("REPORT"):
                        pacman.report()
                    elif command.startswith("PLACE"):
                        args = re.split('\s|,', command)  # split line by space and comma
                        pacman.place(args[1], args[2], args[3])

        # if no valid PLACE commands found then alert user
        if pacman.y_coord is None or pacman.x_coord is None:
            print("Pacman was never placed on the grid.")

main()
