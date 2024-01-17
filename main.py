from graphics import Point
from graphics import Window
from maze import Maze


def main():
    win = Window(800, 600)

    maze_start = Point(50, 50)
    maze = Maze(
        starting_point=maze_start,
        num_rows=13,
        num_cols=14,
        cell_width=50,
        cell_height=40,
        window=win,
        seed=100,
    )

    maze.solve()

    win.wait_for_close()


if __name__ == "__main__":
    main()
