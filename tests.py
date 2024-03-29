import unittest

from graphics import Point
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        cell_width = 20
        cell_height = 16
        m1 = Maze(Point(0, 0), num_rows, num_cols, cell_width, cell_height)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

        end_top_left_x = (num_cols - 1) * cell_width
        end_top_left_y = (num_rows - 1) * cell_height
        end_top_left = Point(end_top_left_x, end_top_left_y)
        end_cell = m1._cells[num_cols - 1][num_rows - 1]
        self.assertEqual(end_top_left, end_cell._top_left)
        self.assertEqual(end_top_left + Point(cell_width, cell_height), end_cell._btm_right)

    def test_entrance_and_exit(self):
        num_cols = num_rows = cell_width = cell_height = 8
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_width, cell_height)
        first_cell = maze._cells[0][0]
        self.assertFalse(first_cell.has_top_wall)
        last_cell = maze._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(last_cell.has_bottom_wall)

    def test_entrance_and_exit_single_cell(self):
        num_cols = num_rows = 1
        cell_width = cell_height = 8
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_width, cell_height)
        first_cell = maze._cells[0][0]
        self.assertFalse(first_cell.has_top_wall)
        last_cell = maze._cells[num_cols - 1][num_rows - 1]
        self.assertFalse(last_cell.has_bottom_wall)
        self.assertFalse(last_cell.has_top_wall)

    def test_maze_ready(self):
        num_cols = 1
        num_rows = 3
        cell_width = cell_height = 10
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_width, cell_height)
        column = maze._cells[0]
        for cell in column:
            self.assertFalse(cell.visited)

        self.assertFalse(column[0].has_bottom_wall)
        self.assertFalse(column[1].has_bottom_wall)
        self.assertFalse(column[1].has_top_wall)
        self.assertFalse(column[2].has_top_wall)

    def test_maze_ready_horizontal_path(self):
        num_cols = 3
        num_rows = 1
        cell_width = cell_height = 10
        maze = Maze(Point(0, 0), num_rows, num_cols, cell_width, cell_height)
        for column in maze._cells:
            self.assertFalse(column[0].visited)

        self.assertFalse(maze._cells[0][0].has_right_wall)
        self.assertFalse(maze._cells[1][0].has_left_wall)
        self.assertFalse(maze._cells[1][0].has_right_wall)
        self.assertFalse(maze._cells[2][0].has_left_wall)


if __name__ == "__main__":
    unittest.main()
