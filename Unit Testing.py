import unittest
import io
from Pacman import Pacman


class UnitTestingPacman(unittest.TestCase):

    def test_place(self):
        test = Pacman()
        test.place(3, 2, "NORTH")
        self.assertEqual(test.x_coord, 3)
        self.assertEqual(test.y_coord, 2)
        self.assertEqual(test.face_direction, "NORTH")

    def test_move(self):
        test = Pacman()
        test.place(3, 2, "NORTH")
        test.move()
        self.assertEqual(test.y_coord, 3)

    def test_left(self):
        test = Pacman()
        test.place(3, 2, "NORTH")
        test.left()
        self.assertEqual(test.face_direction, "WEST")

    def test_right(self):
        test = Pacman()
        test.place(3, 2, "NORTH")
        test.right()
        self.assertEqual(test.face_direction, "EAST")


test = UnitTestingPacman()
test.test_place()
test.test_move()
test.test_left()
test.test_right()