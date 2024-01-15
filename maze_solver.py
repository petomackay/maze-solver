#!/usr/bin/env python3

from tkinter import Tk, BOTH, Canvas


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b


    # TODO: why??
    def draw(self, canvas, color):
        canvas.create_line(
            self.__a.x, self.__a.y, self.__b.x, self.__b.y, fill=color, width=2
        )
        canvas.pack()


class Cell:
    def __init__(self, top_left, btm_right, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__top_left = top_left
        self.__btm_right = btm_right
        self.__window = window

        
    def draw(self, color):
        top_right = Point(self.__btm_right.x, self.__top_left.y)
        btm_left = Point(self.__top_left.x, self.__btm_right.y)
        walls = (
            (self.has_top_wall, self.__top_left, top_right),
            (self.has_right_wall, top_right, self.__btm_right),
            (self.has_bottom_wall, self.__btm_right, btm_left),
            (self.has_left_wall, btm_left, self.__top_left)
        )
        for wall in walls:
            if wall[0]:
                print(f"Drawing wall from: {wall[1].x}, {wall[1].y} to: {wall[2].x}, {wall[2].y}")
                self.__window.draw_line(Line(wall[1], wall[2]), color)
    


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.geometry(f"{width}x{height}")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(master = self.__root, cnf={"bg": "gray"})
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


def main():
    win = Window(800,600)

    Cell(Point(50,50), Point(100,100), win).draw("black")
    Cell(Point(100,100), Point(200,200), win).draw("red")
    Cell(Point(200,200), Point(250,250), win).draw("green")
    border = Cell(Point(2,2), Point(798,598), win)
    border.draw("cyan")

    win.wait_for_close()



if __name__ == "__main__":
    main()

