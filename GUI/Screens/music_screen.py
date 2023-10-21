
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class MusicScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.chronos = clock

        label = ttk.Label(self, text="Music", font=('Helvetica', 48))
        label.pack(side="top", pady=20)