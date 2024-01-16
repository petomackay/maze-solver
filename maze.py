import random

from graphics import Cell, Point
from time import sleep


class Maze:
    def __init__(self,
                 starting_point,
                 num_rows,
                 num_cols,
                 cell_width,
                 cell_height,
                 window=None,
                 seed=None):
        self.__starting_point = starting_point
        self.__num_rows = num_rows 
        self.__num_cols = num_cols
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__window = window
        self.__cells = []
        if seed:
            random.seed(seed)
        self._create_cells()
        self._draw()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)


    def _create_cells(self):
        self._cells = [
            # I know ...
            [Cell(
                Point(self.__starting_point.x + i * self.__cell_width,
                      self.__starting_point.y + j * self.__cell_height ),
                Point(self.__starting_point.x + (i + 1) * self.__cell_width,
                      self.__starting_point.y + (j + 1) * self.__cell_height ),
                self.__window
            ) for j in range(self.__num_rows)] \
            for i in range(self.__num_cols)
        ]


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw("black")
        self._cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self._cells[self.__num_cols - 1][self.__num_rows - 1].draw("black")


    def _break_walls_r(self, x, y):
        directions = (
            (0, -1), # up
            (1, 0),  # right
            (0, 1),  # down
            (-1, 0)  # left
        )
        current_cell = self._cells[x][y]
        current_cell.visited = True

        def is_in_bounds(x, y):
            return 0 <= x < self.__num_cols and 0 <= y < self.__num_rows

        possible_moves = []
        for d in directions:
            new_x = x + d[0]
            new_y = y + d[1]
            if is_in_bounds(new_x, new_y) and not self._cells[new_x][new_y].visited:
                possible_moves.append((new_x, new_y))

        while possible_moves:
            next_coordinates = random.choice(possible_moves)
            n_x = next_coordinates[0]
            n_y = next_coordinates[1]
            possible_moves.remove(next_coordinates)
            next_cell = self._cells[n_x][n_y]
            
            if next_cell.visited:
                continue # visited down the recursion tree already

            if n_x > x:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif n_x < x:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif n_y > y:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            else:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
                
            current_cell.draw("black")
            next_cell.draw("black")
            #self._animate(0.1)

            self._break_walls_r(n_x, n_y)

        return False


    def _draw(self):
        if self.__window is None:
            return
        for column in self._cells:
            for cell in column:
                cell.draw("black")
                self._animate()


    def _animate(self, delay=0.0005):
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(delay)
