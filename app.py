import tkinter as tk
from tkinter import ttk

from pi_clock import PiClock


# TODO : need to inherit the tkinter class
class App():
    
    def __init__(self) -> None:
        self.root = tk.Tk()
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
        self.root.title("PiClock")
        # Make the window borderless (optional)
        self.root.attributes('-fullscreen', True)

        self.style = ttk.Style(self.root)

        # using 3rd party theme
        self.root.call('source', 'Themes/azure/azure.tcl')
        self.root.call('set_theme', 'dark')

        
    def create_labels(self):
        # Create a label for displaying the time
        self.clock_label = tk.Label(self.root, font=('Helvetica', 48))
        self.clock_label.pack(pady=20)  # Add some padding to center the time label



        # Create a frame for the progress bars
        progress_frame = ttk.Frame(self.root )
        progress_frame.pack(pady=20, padx=20, fill=tk.X, side=tk.BOTTOM, anchor=tk.S)  # Stick to the bottom
        
        self.style.configure('TProgressbar', troughcolor='red', background='red', thickness=30)
        
        for label in self.progress_labels:
            tk.Label(progress_frame, text=label).pack()
            progress_bar = ttk.Progressbar(progress_frame, 
                                           style="TProgressbar", 
                                           orient='horizontal', length=300, 
                                           mode='determinate')
            progress_bar.pack(pady=5, fill=tk.X)
            self.progress_bars.append(progress_bar)


if __name__ == '__main__':
    app = App()
    app.start()