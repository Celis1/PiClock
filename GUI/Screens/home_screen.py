import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class HomeScreen(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.clock_label = None
        self.progress_labels = ['Day Progress', 'Month Progress', 
                                'Year Progress', 'Deadline Progress']
        self.progress_bars = []

        self.old_progress_vals = [0, 0, 0, 0]
        

        self._init_page()

    def _init_page(self):
        # creating main clock label
        self.clock_label = ttk.Label(self, font=('Helvetica', 48))
        self.clock_label.pack(pady=25)

        # creating progress bars
        # Create a frame for the progress bars
        progress_frame = ttk.Frame(self)
        progress_frame.pack(pady=20, padx=20, fill=ttk.X, side=ttk.BOTTOM, anchor=ttk.S)  # Stick to the bottom

        # Create a horizontal frame to hold the progress bars
        horizontal_frame = ttk.Frame(progress_frame)
        horizontal_frame.pack(fill=ttk.X)

        color = ['primary', 'primary', 'primary', 'info']
        for i, label in enumerate(self.progress_labels):
            # Create meter widget
            progress_bar = ttk.Meter(horizontal_frame,
                                    metertype='semi',
                                    textright='%',
                                    subtext=label,
                                    textfont=('Helvetica', 20),
                                    subtextfont=('Helvetica', 12),
                                    amountused=0.00,
                                    metersize=210,
                                    meterthickness=5,
                                    bootstyle=color[i])
            progress_bar.pack(fill="both", side=ttk.LEFT, padx=15)  # Pack horizontally with some padding
            self.progress_bars.append(progress_bar)

