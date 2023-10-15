import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class AlarmScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # self.label = ttk.Label(self, text="Page 2")
        # self.label.pack(fill=tk.BOTH, expand=True)