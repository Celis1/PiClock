import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from GUI.Screens import *

import random
from pi_clock import PiClock

class App(ttk.Window):
    def __init__(self):
        super().__init__(title="Life Clock", 
                         themename="darkly")
        # setting the app to fullscreen
        self.attributes('-fullscreen', True)
        # disabling the cursor
        # TODO : enable this when the app is ready
        # self.configure(cursor="none")


        # Create a ttk.Notebook to manage multiple pages
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)


        # Customize the font for the tab labels
        style = Style()
        style.configure('TNotebook.Tab', font=('Helvetica', 32) )
        # center tabs on the page
        style.configure("TNotebook", tabposition='n')
        # change the background color of the tab adding space between the top of the screen
        style.configure('TNotebook', bordercolor='darkly', padding=5)
        
        # TODO : clean up this mess

        # Add the HomeScreen and Page2 frames to the self.notebook
        self.home_screen = HomeScreen(self.notebook)
        self.alarm_screen = AlarmScreen(self.notebook)
        self.stats_screen = StatsScreen(self.notebook)
        self.notebook.add(self.alarm_screen, text="Alarm")
        self.notebook.add(self.home_screen, text="Home")
        self.notebook.add(self.stats_screen, text="Stats")

        self.notebook.select(self.home_screen)

        # adding my clock class
        self.pi_clock = PiClock()
        self.pi_clock.start()

        # initializing the text for the app
        self.update_progress_bars()


    # Function to update progress bars
    # TODO : This is everywhere, make sure it belongs in this class or the homescreen!
    def update_progress_bars(self):

        # Get the current time and progress
        info = self.pi_clock.update_time()
        # checking if its wake up time
        # print('waiting')
        if self.pi_clock.check_alarm():
            print("********Alarm time!")
            self.activate_alarm()


        self.home_screen.clock_label.config(text=info['time'])  

        for i, label in enumerate(self.home_screen.progress_labels):
            lebel_text = label.lower().replace(' ', '_')
            value = info[lebel_text] * 100
            # round to nearest 2 decimal places
            value = round(value, 2)
            # only update if the value has changed
            if value != self.home_screen.old_progress_vals[i]:
                self.home_screen.old_progress_vals[i] = value
                time_left = info[lebel_text.replace('progress', 'left')]
                # TODO : Come up with a better way to do this
                if i == 0:
                    text = f'{label}:\nhours left {time_left}h'
                else:
                    text = f'{label}:\ndays left {time_left}d'
                self.home_screen.progress_bars[i].configure(amountused = value, subtext=text )
                self.home_screen.progress_bars[i].update()
        self.after(10, self.update_progress_bars)

    # TODO : This should be in the alarm screen class
    def alarm(self):
        colors = ['primary', 'secondary', 'success', 'info', 'warning', 'danger', 'light', 'dark']
        # pick random color
        color = random.choice(colors)

        if self.pi_clock.keep_playing:
            self.wake_label.config(bootstyle=color)
            if not self.pi_clock.yt_music.is_playing():
                self.after(1000, self.alarm)
                return
            else:
                self.pi_clock.yt_music.play_song(self.pi_clock.wake_url)
                self.after(1000, self.alarm)
                return
        else:
            return
        
    # TODO : This should be in the alarm screen class
    def activate_alarm(self):
        self.pi_clock.keep_playing = True
        self.notebook.select(self.alarm_screen)

        self.wake_label = ttk.Label(self.alarm_screen, text="WAKE UP!", font=('Helvetica', 64))
        self.wake_label.pack(padx=20, pady=25)
        ttk.Style().configure('danger.TButton', font=('Helvetica', 64))

        self.alarm_close_button = ttk.Button(self.alarm_screen, 
                                  text="Close", 
                                  width=30,
                                  style='danger.TButton',
                                  command=self.deactivate_alarm)
        self.alarm_close_button.pack(pady=30,side=ttk.BOTTOM, anchor=ttk.S)
        
        # calling the music
        self.alarm()

    # TODO : This should be in the alarm screen class
    def deactivate_alarm(self):
        # end the music
        self.pi_clock.yt_music.stop_song()
        self.pi_clock.keep_playing = False

        # destroy the pop-up window
        self.alarm_close_button.destroy()
        self.wake_label.destroy()
        self.wake_label = None

        # TODO : replace destroy with this so we dont have to save widgets in class
        # for widgets in frame.winfo_children():
        #     widgets.destroy()

        # return to homepage 
        self.notebook.select(self.home_screen)

if __name__ == "__main__":
    # style = Style(theme="darkly")
    app = App()
    app.mainloop()