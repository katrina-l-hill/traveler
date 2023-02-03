"""Import tkinter module."""
from tkinter import *

# from tkinter import ttk
# from tkinter.messagebox import showinfo


class Window:
    """Create Window class to start."""

    # master is the root/main window

    def __init__(self, master):
        # create a frame in the main window
        frame = Frame(master)
        # display it on the main screen
        frame.pack()

        self.print_button = Button(
            frame, text="Print Message", command=self.print_message
        )
        self.print_button.pack(side=LEFT)

        self.quit_button = Button(frame, text="Quit", command=frame.quit)
        self.quit_button.pack(side=LEFT)

    def print_message(self):
        """Prints the message."""
        print("Print message to the console")


root = Tk()
world = Window(root)
root.mainloop()
