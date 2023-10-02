# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from pi_clock import PiClock


# TODO : need to inherit the tkinter class
class App():
    
    def __init__(self) -> None:
        self.root = ttk.Window(themename="darkly")
        self.pi_clock = PiClock()

        self.style = None

        self.clock_label = None
        self.progress_labels = ['Day Progress', 'Month Progress', 'Year Progress', 'Deadline Progress']
        self.progress_bars = []
                

    def start(self):
        self._configure_root()
        self.create_labels()
        self.update_progress_bars()

        # self.pi_clock.wake_up()
        # running tkinter mainloop
        self.root.mainloop()

    # Function to update progress bars
    def update_progress_bars(self):

        # Get the current time and progress
        info = self.pi_clock.update_time()

        self.clock_label.config(text=info['time'])  

        for i, label in enumerate(self.progress_labels):
            self.progress_bars[i]['value'] = info[label.lower().replace(' ', '_')] * 100
            self.progress_bars[i].update()
        self.root.after(10, self.update_progress_bars)

    def _configure_root(self):
        # self.style = ttk.Style(self.root)


        self.root.title("PiClock")
        # Make the window borderless (optional)
        self.root.attributes('-fullscreen', True)

        # using 3rd party theme
        self.root.call('source', 'Themes/sun-valley/sun-valley.tcl')
        self.root.call('set_theme', 'dark')
        # self.style.theme_use('clam') 

        # self.style.configure("CustomTProgressbar",
        #                      troughcolor ='blue', 
        #                      background='green') 



        
    def create_labels(self):
        # Create a label for displaying the time
        self.clock_label = ttk.Label(self.root, font=('Helvetica', 48))
        self.clock_label.pack(pady=20)  # Add some padding to center the time label


        # Create a frame for the progress bars
        progress_frame = ttk.Frame(self.root )
        progress_frame.pack(pady=20, padx=20, fill=ttk.X, side=ttk.BOTTOM, anchor=ttk.S)  # Stick to the bottom
        
        for label in self.progress_labels:
            ttk.Label(progress_frame, text=label).pack()
            progress_bar = ttk.Progressbar(progress_frame, 
                                           orient='horizontal', length=300,
                                           mode='determinate')
            progress_bar.pack(pady=5, fill=ttk.X)
            self.progress_bars.append(progress_bar)

        # create meter widget
        meter = ttk.Meter(self.root,
                            metertype = 'semi',
                            textright='%',
                            # stripethickness = 5,
                            subtext="miles per hour",
                            textfont=('Helvetica', 25),
                            subtextfont=('Helvetica', 12),
                            amountused=65,
                            metersize=180,
                            meterthickness=15)
        
        meter.pack(pady=20, padx=20, fill=ttk.X, side=ttk.BOTTOM, anchor=ttk.S)


if __name__ == '__main__':
    app = App()
    app.start()