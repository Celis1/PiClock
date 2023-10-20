import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class StatsScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.chronos = clock
        # self.label = ttk.Label(self, text="Page 3")
        # self.label.pack(fill=tk.BOTH, expand=True)


        # Testing matplotlib
        fig = Figure(figsize=(6, 4), dpi=100)
        # Create a subplot
        ax = fig.add_subplot(111)

        # Plot your data (e.g., a simple example)
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]
        ax.plot(x, y, label='Sample Data')

        # Set labels and title
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_title('Matplotlib Plot')
        ax.legend()

        # Create a FigureCanvasTkAgg widget
        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack()

