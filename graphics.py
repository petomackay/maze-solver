from tkinter import BOTH
from tkinter import Canvas
from tkinter import Tk

BACKGROUND_COLOR = "gray"


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def halfway(self, other):
        x_delta = (other.x - self.x) // 2
        y_delta = (other.y - self.y) // 2
        return Point(self.x + x_delta, self.y + y_delta)

    def __str__(self):
        return f"[{self.x}, {self.y}]"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


class Line:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    # TODO: why??
    def draw(self, canvas, color):
        canvas.create_line(self.__a.x, self.__a.y, self.__b.x, self.__b.y, fill=color, width=2)
        canvas.pack()


class Cell:
    def __init__(self, top_left, btm_right, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._top_left = top_left
        self._btm_right = btm_right
        self.__window = window
        self.visited = False

    def get_center(self):
        return self._btm_right.halfway(self._top_left)

    def draw(self, color):
        if self.__window is None:
            return
        top_right = Point(self._btm_right.x, self._top_left.y)
        btm_left = Point(self._top_left.x, self._btm_right.y)
        walls = (
            (self.has_top_wall, self._top_left, top_right),
            (self.has_right_wall, top_right, self._btm_right),
            (self.has_bottom_wall, self._btm_right, btm_left),
            (self.has_left_wall, btm_left, self._top_left),
        )
        for wall in walls:
            if wall[0]:
                # print(f"Drawing wall from: {wall[1]} to: {wall[2]}")
                self.__draw_line(Line(wall[1], wall[2]), color)
            else:
                self.__draw_line(Line(wall[1], wall[2]), BACKGROUND_COLOR)

    def draw_move(self, to_cell, undo=False):
        color = "pink" if undo else "red"
        self.__draw_line(Line(self.get_center(), to_cell.get_center()), color)

    def __draw_line(self, line, color):
        self.__window.draw_line(line, color)


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(master=self.__root, cnf={"bg": BACKGROUND_COLOR})
        self.canvas.pack(fill=BOTH, expand=True)

        self.is_running = False

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.is_running = True
        while self.is_running:
            self.redraw()

    def close(self):
        self.is_running = False

    def draw_line(self, line, color):
        line.draw(self.canvas, color)
