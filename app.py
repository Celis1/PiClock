# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import random

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

        self.old_progress_vals = [0, 0, 0, 0]
                

    def start(self):
        self.pi_clock.start()
        self._configure_root()
        self.create_labels()
        self.update_progress_bars()

        # running tkinter mainloop
        self.root.mainloop()

    # Function to open the pop-up window
    def open_popup(self):
        self.pi_clock.keep_playing = True
        self.popup = ttk.Toplevel(self.root)
        self.popup.title("Alarm")

        # Add widgets to the pop-up window
        self.wake_label = ttk.Label(self.popup, text="WAKE UP!", font=('Helvetica', 64))
        self.wake_label.pack(padx=20, pady=20)

        close_button = ttk.Button(self.popup, text="Close", command=self.close_popup)
        close_button.pack(pady=10)
        self.alarm()

    def alarm(self):
        colors = ['primary', 'secondary', 'success', 'info', 'warning', 'danger', 'light', 'dark']
        # pick random color
        color = random.choice(colors)

        self.wake_label.config(bootstyle=color)

        if self.pi_clock.keep_playing:
            if not self.pi_clock.yt_music.is_playing():
                print('currnetly playing')
                self.root.after(1000, self.alarm)
                return
            else:
                self.pi_clock.yt_music.play_song(self.pi_clock.wake_url)
                self.root.after(1000, self.alarm)
                return


    def close_popup(self):
        # destroy the pop-up window
        self.popup.destroy()
        # end the music
        self.pi_clock.yt_music.stop_song()
        self.pi_clock.keep_playing = False


    # Function to update progress bars
    def update_progress_bars(self):

        # Get the current time and progress
        info = self.pi_clock.update_time()
        if self.pi_clock.check_time():
            #TODO : write stuff
            self.open_popup()


        self.clock_label.config(text=info['time'])  

        for i, label in enumerate(self.progress_labels):
            lebel_text = label.lower().replace(' ', '_')
            value = info[lebel_text] * 100
            # round to nearest 2 decimal places
            value = round(value, 2)
            # only update if the value has changed
            if value != self.old_progress_vals[i]:
                self.old_progress_vals[i] = value
                time_left = info[lebel_text.replace('progress', 'left')]
                # TODO : Come up with a better way to do this
                if i == 0:
                    text = f'{label}:\nhours left {time_left}h'
                else:
                    text = f'{label}:\ndays left {time_left}d'
                self.progress_bars[i].configure(amountused = value, subtext=text )
                self.progress_bars[i].update()
        self.root.after(10, self.update_progress_bars)

    def _configure_root(self):
        # self.style = ttk.Style(self.root)
        self.root.title("PiClock")
        # Make the window borderless (optional)
        self.root.attributes('-fullscreen', True)

        
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
                                    textfont=('Helvetica', 20),
                                    subtextfont=('Helvetica', 12),
                                    amountused=0.00,
                                    metersize=210,
                                    meterthickness=5,
                                    bootstyle=color[i])
            progress_bar.pack(fill="both", side=ttk.LEFT, padx=15)  # Pack horizontally with some padding
            self.progress_bars.append(progress_bar)


if __name__ == '__main__':
    app = App()
    app.start()