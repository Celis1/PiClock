import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class StatsScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.chronos = clock
        self.label = ttk.Label(self, text="Page 3")
        self.label.pack(fill=tk.BOTH, expand=True)
