import tkinter as tk

class MyWidget:
    def __init__(self, parent, starting_row, starting_col):
        self.parent = parent

        self.entry_var = tk.StringVar()
        self.entry_var.set("0")

        self.entry = tk.Entry(parent, textvariable=self.entry_var, state="readonly", width=5)
        self.entry.grid(row=starting_row, column=starting_col, padx=5, pady=10)

        self.increment_button = tk.Button(parent, text="↑", command=self.increment, padx=0)
        self.increment_button.grid(row=starting_row, column=starting_col + 1, padx=0, pady=0)

        self.decrement_button = tk.Button(parent, text="↓", command=self.decrement, padx=0)
        self.decrement_button.grid(row=starting_row, column=starting_col + 2, padx=0, pady=0)

        self.set_to_30_button = tk.Button(parent, text="30", command=self.set_to_30, padx=0)
        self.set_to_30_button.grid(row=starting_row, column=starting_col + 3, padx=0, pady=0)

    def increment(self):
        current_value = int(self.entry_var.get() or 0)
        self.entry_var.set(str(current_value + 1))

    def decrement(self):
        current_value = int(self.entry_var.get() or 0)
        if current_value > 0:
            self.entry_var.set(str(current_value - 1))

    def set_to_30(self):
        self.entry_var.set("30")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Custom Widget Example")

    widget1 = MyWidget(root, 0, 0)
    widget2 = MyWidget(root, 1, 0)

    root.mainloop()
