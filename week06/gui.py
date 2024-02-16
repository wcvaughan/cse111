# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

import tkinter as tk
from tkinter import Frame, Label, Button
from number_entry import IntEntry
import math


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Pendulum Period Calculator")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "length:"
    lbl_length = Label(frm_main, text="Pendulum length (1 - 100):")

    # Create an integer entry box where the user will enter her length.
    ent_length = IntEntry(frm_main, width=4, lower_bound=1, upper_bound=100)

    # Create a label that displays "meters"
    lbl_length_units = Label(frm_main, text="meters")

    # Create a label that displays "time:"
    lbl_time = Label(frm_main, text="time:")

    # Create labels that will display the results.
    lbl_period = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="cycles/second")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_length.grid(      row=0, column=0, padx=3, pady=3)
    ent_length.grid(      row=0, column=1, padx=3, pady=3)
    lbl_length_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_time.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_period.grid(      row=1, column=1, padx=3, pady=3)
    lbl_rate_units.grid(row=1, column=2, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the swing time of a pendulum.
        """
        try:
            # Get the length of the pendulum.
            length = ent_length.get()

            gravity = 9.8

            # Compute period of the pendulum
            period = 2 * math.pi * math.sqrt(length / gravity)

            # Display the pendulum period time.
            lbl_period.config(text=f"{period:.0f}")

        except ValueError:
            # When the user deletes all the digits in the length
            # entry box, labels.
            lbl_period.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_length.clear()
        lbl_period.config(text="")
        ent_length.focus()

    # Bind the calculate function to the length entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_length.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the length entry box.
    ent_length.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
