import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# TODO : this is all done with tkinter use ttkbootstrap
class InputeTimeWidget:
    def __init__(self, parent, starting_row, starting_col, label_text):
        self.parent = parent

        # Create a label for the widget
        label = tk.Label(parent, text=label_text)
        label.grid(row=starting_row, column=starting_col, padx=5, pady=2)

        self.entry_var = tk.StringVar()
        self.entry_var.set("0")

        self.entry = tk.Entry(parent, textvariable=self.entry_var, state="readonly", width=5)
        self.entry.grid(row=starting_row, column=starting_col + 1, padx=5, pady=2)

        self.increment_button = tk.Button(parent, text="↑", command=self.increment, padx=0)
        self.increment_button.grid(row=starting_row, column=starting_col + 2, padx=0, pady=0)

        self.decrement_button = tk.Button(parent, text="↓", command=self.decrement, padx=0)
        self.decrement_button.grid(row=starting_row, column=starting_col + 3, padx=0, pady=0)
        
        self.set_to_30_button = tk.Button(parent, text="30", command=self.set_to_30, padx=0)
        self.set_to_30_button.grid(row=starting_row, column=starting_col + 4, padx=0, pady=0)


    def increment(self):
        current_value = int(self.entry_var.get() or 0)
        self.entry_var.set(str(current_value + 1))

    def decrement(self):
        current_value = int(self.entry_var.get() or 0)
        if current_value > 0:
            self.entry_var.set(str(current_value - 1))

    def set_to_30(self):
        self.entry_var.set("30")

# TODO : Clean all this code
class WorkoutScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.clock = clock

        # Create a label
        label = tk.Label(self, text="Workout Tracker", font=('Helvetica', 48))
        label.grid(row=0, column=0, columnspan=3, pady=(20, 0))

        self.selected_workouts = []
        for i, workout in enumerate(self.clock.workout.workouts):
            workout_text = workout.capitalize() 
            checkbox = tk.Checkbutton(self, text=workout_text, 
                                      variable=tk.BooleanVar(), 
                                      font=('Helvetica', 24),
                                      )

            # Calculate row and column based on index i
            row = (i // 3) + 1
            column = i % 3

            checkbox.grid(row=row + 1, column=column, padx=10)
            self.selected_workouts.append((workout, checkbox))

        # create a new frame that is inside this page
        frame = ttk.Frame(self)
        curr_row = 5
        frame.grid(row=curr_row, column=1, padx=10)

        # Create and place InputeTimeWidget instances
        hours_widget = InputeTimeWidget(frame, curr_row, 0, "Hours")
        minutes_widget = InputeTimeWidget(frame, curr_row+1, 0, "Minutes")

        # Create a button to save the workout
        # TODO : add saving workout to app
        # save_button = ttk.Button(frame, text="Save Workout", command= lambda : self.clock.workout.set_workout())
        # save_button.grid(row=curr_row+2, column=1, pady=10)

        # Center-align the grid
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)


