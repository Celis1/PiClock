import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

import random

class AlarmScreen(ttk.Frame):
    def __init__(self, parent, clock):
        super().__init__(parent)
        self.chronos = clock

        # TODO : Move this 
        # Create a label
        label = tk.Label(self, text="Alarms", font=('Helvetica', 48))
        label.pack(side="top", pady=20)

    def create_alarm_widgets(self):
        self.wake_label = ttk.Label(self, text="WAKE UP!", font=('Helvetica', 64))
        self.wake_label.pack(padx=20, pady=25)
        ttk.Style().configure('danger.TButton', font=('Helvetica', 64))

        self.alarm_close_button = ttk.Button(self, 
                                  text="Close", 
                                  width=30,
                                  style='danger.TButton',
                                  command=self.deactivate_alarm)
        self.alarm_close_button.pack(pady=30,side=ttk.BOTTOM, anchor=ttk.S)

    def destroy_alarm_widgets(self):
        self.alarm_close_button.destroy()
        self.wake_label.destroy()
        self.wake_label = None
        # TODO : replace destroy with this so we dont have to save widgets in class
        # for widgets in frame.winfo_children():
        #     widgets.destroy()

    def alarm(self):
        colors = ['primary', 'secondary', 'success', 'info', 'warning', 'danger', 'light', 'dark']
        # pick random color
        color = random.choice(colors)

        if self.chronos.keep_playing:
            self.wake_label.config(bootstyle=color)
            if not self.chronos.yt_music.is_playing():
                self.after(1000, self.alarm)
                return
            else:
                self.chronos.yt_music.play_song(self.chronos.wake_url)
                self.after(1000, self.alarm)
                return
        else:
            return
        
    def activate_alarm(self):
        self.chronos.keep_playing = True
        self.master.select(0)
        self.create_alarm_widgets()

        # calling the music
        self.alarm()
        
    def deactivate_alarm(self):
        # end the music
        self.chronos.yt_music.stop_song()
        self.chronos.keep_playing = False

        self.destroy_alarm_widgets()

        # return to homepage
        self.master.select(1)

        # Starting morning routine
        self.chronos.start_morning_routine()
