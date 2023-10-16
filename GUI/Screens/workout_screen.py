import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class WorkoutScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.clock = clock
        self.label = ttk.Label(self, text="Workout")
        self.label.pack(fill=tk.BOTH, expand=True)
