from graphics import Cell, Point
from time import sleep

class Maze:
    def __init__(self,
                 starting_point,
                 num_rows,
                 num_cols,
                 cell_width,
                 cell_height,
                 window=None):
        self.__starting_point = starting_point
        self.__num_rows = num_rows 
        self.__num_cols = num_cols
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__window = window
        self.__cells = []
        self._create_cells()
        self._draw()


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


    def _draw(self):
        if self.__window is None:
            return
        for column in self._cells:
            for cell in column:
                cell.draw("black")
                self._animate()


    def _animate(self):
        if self.__window is None:
            return
        self.__window.redraw()
        sleep(0.05)
