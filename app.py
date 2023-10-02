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
            lebel_text = label.lower().replace(' ', '_')
            value = info[lebel_text] * 100
            # round to nearest 2 decimal places
            value = round(value, 2)
            time_left = info[lebel_text.replace('progress', 'left')]
            text = f'{label}: {time_left}'

            self.progress_bars[i].configure(amountused = value, subtext=text )
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
        # Add some padding to center the time label
        self.clock_label.pack(pady=25)  

        # Create a frame for the progress bars
        progress_frame = ttk.Frame(self.root)
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
                                    textfont=('Helvetica', 25),
                                    subtextfont=('Helvetica', 16),
                                    amountused=0.00,
                                    metersize=350,
                                    meterthickness=5,
                                    bootstyle=color[i])
            progress_bar.pack(fill="both", side=ttk.LEFT, padx=15)  # Pack horizontally with some padding
            self.progress_bars.append(progress_bar)


if __name__ == '__main__':
    app = App()
    app.start()