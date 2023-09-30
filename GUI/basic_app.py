import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Function to update the clock display
def update_clock():
    curr_time = datetime.now().strftime('%H:%M:%S')
    clock_label.config(text=curr_time)
    root.after(1000, update_clock)

# Initialize the Tkinter window
root = tk.Tk()
root.title("Digital Clock with Progress Bars")

# Configure the dark mode theme
root.configure(bg='#1e1e1e')  # Set background color to dark gray
ttk.Style().configure('TLabel', background='#1e1e1e', foreground='#ffffff')  # Set label text color to white
ttk.Style().configure('TFrame', background='#1e1e1e')  # Set frame background color to dark gray
ttk.Style().configure('TButton', background='#444444', foreground='#ffffff')  # Set button colors

# Create a label for displaying the time
clock_label = ttk.Label(root, font=('Helvetica', 48))
clock_label.pack(pady=20)  # Add some padding to center the time label

# Create a frame for the progress bars
progress_frame = ttk.Frame(root)
progress_frame.pack(pady=20)

# Create progress bars
progress_labels = ['Day Progress', 'Month Progress', 'Year Progress', 'Deadline Progress']
progress_bars = []

for label in progress_labels:
    ttk.Label(progress_frame, text=label).pack()
    progress_bar = ttk.Progressbar(progress_frame, orient='horizontal', length=300, mode='determinate')
    progress_bar.pack(pady=5)
    progress_bars.append(progress_bar)

# Function to update progress bars
def update_progress_bars():
    for i, label in enumerate(progress_labels):
        progress_bars[i]['value'] = info[label.lower().replace(' ', '_')]
        progress_bars[i].update()
    root.after(60000, update_progress_bars)  # Update progress bars every minute

# Call the update_clock and update_progress_bars functions to display time and progress
update_clock()
update_progress_bars()

# Run the Tkinter main loop
root.mainloop()
