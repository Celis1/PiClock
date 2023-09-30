import tkinter as tk
from tkinter import ttk

from pi_clock import PiClock

borderImageData = '''
    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
'''

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

        self.style = ttk.Style(self.root)

        # using 3rd party theme
        self.root.call('source', 'Themes/azure/azure.tcl')
        self.root.call('set_theme', 'dark')

        borderImage = tk.PhotoImage("borderImage", data=borderImageData)

        self.style.element_create("RoundedFrame",
                        "image",
                        borderImage,
                        # ("focus", focusBorderImage),
                        border=16,
                        sticky="nsew")
        
        self.style.layout("RoundedFrame",
                        [("RoundedFrame", {"sticky": "nsew"})])
        
    def create_labels(self):
        # Create a label for displaying the time
        self.clock_label = tk.Label(self.root, font=('Helvetica', 48))
        self.clock_label.pack(pady=20)  # Add some padding to center the time label



        # Create a frame for the progress bars
        progress_frame = ttk.Frame(self.root, style="RoundedFrame" )
        progress_frame.pack(pady=20, padx=20, fill=tk.X, side=tk.BOTTOM, anchor=tk.S)  # Stick to the bottom
        

        for label in self.progress_labels:
            tk.Label(progress_frame, text=label).pack()
            progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', length=300, mode='determinate')
            progress_bar.pack(pady=5, fill=tk.X)
            self.progress_bars.append(progress_bar)


if __name__ == '__main__':
    app = App()
    app.start()