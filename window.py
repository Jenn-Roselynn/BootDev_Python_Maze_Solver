from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        # Connecting the window's close button to our close method
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        # Refreshes the GUI to show new changes
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        # Keeps the window open until the user closes it
        self.__is_running = True
        while self.__is_running:
            self.redraw()

    def close(self):
        # Signals the loop in wait_for_close to stop
        self.__is_running = False

    def draw_line(self, line, fill_color="black"):
        # This will be used once we have our Line class defined
        line.draw(self.__canvas, fill_color)