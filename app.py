import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from GUI.Screens import *

from pi_clock import LifeClock

class App(ttk.Window):
    def __init__(self):
        super().__init__(title="Life Clock", 
                         themename="darkly")
        # setting the app to fullscreen
        self.attributes('-fullscreen', True)

        self.home_screen = None
        self.alarm_screen = None
        self.workout_screen = None
        self.stats_screen = None

        # adding my clock class
        self.chronos = LifeClock()
        self.chronos.start()

        # adding the style
        self._configure_style()

        # Create a notebook to manage multiple pages
        self.notebook = self._configure_notebook()
        
        # initializing the text for the app
        self.update_ticks()

    def update_ticks(self):
        '''
        Main update function for app control
        '''
        # checking if its wake up time
        if self.chronos.check_alarm():
            print("********Alarm time!")
            self.alarm_screen.activate_alarm()

        self.home_screen.update_progress_bars()
        self.after(10, self.update_ticks)

    def _configure_notebook(self):
        '''
        All configuration for the notebook
        '''
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Adding screens to notebook
        self.home_screen = HomeScreen(notebook, self.chronos)
        self.alarm_screen = AlarmScreen(notebook, self.chronos)
        self.workout_screen = WorkoutScreen(notebook, self.chronos)
        self.stats_screen = StatsScreen(notebook, self.chronos)

        # adding the screens to the notebook
        notebook.add(self.alarm_screen, text="Alarm")
        notebook.add(self.home_screen, text="Home")
        notebook.add(self.workout_screen, text="Workout")
        notebook.add(self.stats_screen, text="Stats")

        notebook.select(self.home_screen)
        return notebook

    def _configure_style(self):
        '''
        All configuration for the style
        '''
        # Customize the font for the tab labels
        style = Style()
        style.configure('TNotebook.Tab', font=('Helvetica', 32) )
        # center tabs on the page
        style.configure("TNotebook", tabposition='n')
        # change the background color of the tab adding space between the top of the screen
        style.configure('TNotebook', bordercolor='darkly', padding=5)



if __name__ == "__main__":
    app = App()
    app.mainloop()