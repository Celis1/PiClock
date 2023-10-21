# import tkinter as tk
# from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import threading

# TODO : this is all done with tkinter use ttkbootstrap
class InputeTimeWidget:
    def __init__(self, parent, starting_row, starting_col, label_text):
        self.parent = parent

        # Create a label for the widget
        label = ttk.Label(parent, text=label_text, font=('Helvetica', 24))
        label.grid(row=starting_row, column=starting_col, padx=5, pady=2)

        self.entry_var = ttk.StringVar()
        self.entry_var.set("0")

        self.entry = ttk.Entry(parent, 
                               textvariable=self.entry_var, font=('Helvetica', 24),
                               state="readonly", width=5)
        self.entry.grid(row=starting_row, column=starting_col + 1, padx=5, pady=2)

        self.increment_button = ttk.Button(parent, bootstyle="info-outline",
                                           text="↑", command=self.increment,)
        self.increment_button.grid(row=starting_row, column=starting_col + 2, padx=5, pady=5)

        self.decrement_button = ttk.Button(parent, bootstyle="info-outline",
                                           text="↓", command=self.decrement)
        self.decrement_button.grid(row=starting_row, column=starting_col + 3, padx=5, pady=5)
        
        self.set_to_30_button = ttk.Button(parent, bootstyle="info-outline",
                                           text="+10", command=self.add_10)
        self.set_to_30_button.grid(row=starting_row, column=starting_col + 4, padx=5, pady=5)

        self.set_to_30_button = ttk.Button(parent, bootstyle="info-outline",
                                           text="-10", command=self.sub_10)
        self.set_to_30_button.grid(row=starting_row, column=starting_col + 5, padx=5, pady=5)


    def increment(self):
        current_value = int(self.entry_var.get()) + 1
        if current_value > 59:
            current_value = 59
        self.entry_var.set(str(current_value ))

    def decrement(self):
        current_value = int(self.entry_var.get() or 0)
        if current_value > 0:
            self.entry_var.set(str(current_value - 1))

    def add_10(self):
        value = int(self.entry_var.get()) + 10
        if value > 59:
            value = 59
        self.entry_var.set(value)

    def sub_10(self):
        value = int(self.entry_var.get()) - 10
        if value < 0:
            value = 0
        self.entry_var.set(value)

# TODO : Clean all this code
class WorkoutScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.chronos = clock
        

        # Create a label
        label = ttk.Label(self, text="Workout Tracker", font=('Helvetica', 48))
        label.grid(row=0, column=0, columnspan=3, pady=(20, 0))

        self.selected_workouts = []
        for i, workout in enumerate(self.chronos.workout.workouts):
            workout_text = workout.capitalize()

            checkbox_var = ttk.BooleanVar(value=False)
            checkbox = ttk.Checkbutton(self,
                                        text=workout_text,
                                        bootstyle="info-toolbutton",
                                        variable=checkbox_var,
                                        # font=('Helvetica', 24),
                                        width = 15,
                                      )
            
            # Calculate row and column based on index i
            row = (i // 3) + 1
            column = i % 3

            checkbox.grid(row=row + 1, column=column, padx=10, pady=10)
            self.selected_workouts.append((workout, checkbox))

        # create a new frame that is inside this page
        frame = ttk.Frame(self)
        curr_row = 5
        frame.grid(row=curr_row, column=1, padx=10, pady=20)

        # Create and place InputeTimeWidget instances
        hours_widget = InputeTimeWidget(frame, curr_row, 0, "Hours")
        minutes_widget = InputeTimeWidget(frame, curr_row+1, 0, "Minutes")

        # Create a button to save the workout
        # TODO : add saving workout to app
        # create a new frame that is inside this page
        other_frame = ttk.Frame(self)
        curr_row = 5
        other_frame.grid(row=curr_row+1, column=1, padx=10, pady=20)
        save_button = ttk.Button(other_frame, text="Save Workout",
                                bootstyle="success-outline",
                                width=20,
                                command= lambda : self.save_workout_button(self.selected_workouts,
                                        [hours_widget.entry_var, minutes_widget.entry_var]))
        save_button.grid(row=1, column=1, pady=5)

        self.info_label = ttk.Label(self, 
                                bootstyle = 'warning',
                                text="", 
                                font=('Helvetica', 16))
        self.info_label.grid(row=curr_row+2, column=1, pady=15)

        # Center-align the grid
        for i in range(3):
            self.grid_columnconfigure(i, weight=1)


    def save_workout_button(self, workout_widgets, time_blocks):
        def reset_text():
            self.info_label.configure(text="")

        selected_workouts = [i for i,j in workout_widgets if j.instate(['selected'])]
        print(selected_workouts)
        some_time = [time_blocks[0].get(),time_blocks[1].get()]
        if selected_workouts == []:
            text = "**No workouts selected**"
            self.info_label.configure(text=text)
            # TODO : make this stand alone function
            # create a thread that will clear the text after 1min
            thread = threading.Timer(10, reset_text)
            thread.start()
            return
        
        elif  some_time == ['0','0']:
            text = "**No time session selected**"
            self.info_label.configure(text=text)
            # create a thread that will clear the text after 1min
            thread = threading.Timer(10, reset_text)
            thread.start()
            return
        
        time_session = ':'.join(some_time) + ':00'
        print(time_session)

        self.chronos.workout.set_workout(selected_workouts, time_session)

        # reset all selected checkboxes
        for i,j in workout_widgets:
            j.state(['!selected'])        

        # reset time widgets
        for i in time_blocks:
            i.set('0')

        text = "**successfully added workout! **"
        self.info_label.configure(text=text)

        # create a thread that will clear the text after 1min
        thread = threading.Timer(10, reset_text)
        thread.start()