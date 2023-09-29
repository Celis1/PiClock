import tkinter as tk
from tkinter import ttk
from datetime import datetime

def start_loading():
    loading_bar.start(10)  # Start the loading animation
    root.after(3000, stop_loading)  # Simulate loading for 3 seconds

def stop_loading():
    loading_bar.stop()  # Stop the loading animation

def update_datetime():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%I:%M:%S %p\n%A, %B %d, %Y")
    datetime_label.config(text="Current Date and Time:\n" + formatted_datetime)
    root.after(1000, update_datetime)  # Update the datetime every 1 second

root = tk.Tk()
root.title("Date and Time Display App")
root.geometry("400x200")
root.configure(bg="black")  # Set the default background color to black

datetime_label = tk.Label(root, text="Current Date and Time: 00:00:00 AM\nDay, Month Day, Year",
                          font=("Helvetica", 14), fg="white", justify="center")
datetime_label.pack(pady=20)

loading_frame = ttk.Frame(root)
loading_frame.pack()

loading_bar = ttk.Progressbar(loading_frame, mode="indeterminate", length=200)
loading_bar.grid(row=0, column=0, padx=10, pady=10)

start_loading()  # Start loading when the app is launched
update_datetime()  # Update the datetime label

root.mainloop()
