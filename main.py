from graphics import Window, Point
from maze import Maze


def main():
    win = Window(800,600)

    maze_start = Point(50,50) 
    maze = Maze(
        starting_point=maze_start,
        num_rows=23,
        num_cols=24,
        cell_width=50,
        cell_height=40,
        window=win,
        seed=100
    )

    win.wait_for_close()



if __name__ == "__main__":
    main()

