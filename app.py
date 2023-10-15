import tkinter as tk
from ttkbootstrap import Style
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from GUI.Screens import *

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
        notebook = ttk.Notebook(self)
        notebook.pack(fill=tk.BOTH, expand=True)


        # Customize the font for the tab labels
        style = Style()
        style.configure('TNotebook.Tab', font=('Helvetica', 32) )
        # center tabs on the page
        style.configure("TNotebook", tabposition='n')
        # change the background color of the tab adding space between the top of the screen
        style.configure('TNotebook', bordercolor='darkly', padding=5)
        


        # Add the HomeScreen and Page2 frames to the notebook
        self.homepage = HomeScreen(notebook)
        self.page2 = AlarmScreen(notebook)
        self.page3 = StatsScreen(notebook)
        notebook.add(self.page2, text="Page 2")
        notebook.add(self.homepage, text="Home")
        notebook.add(self.page3, text="Page 3")

        notebook.select(self.homepage)


if __name__ == "__main__":
    # style = Style(theme="darkly")
    app = App()
    app.mainloop()