import tkinter as tk
from datetime import timedelta


class CountdownApp:
    def __init__(self, master):
        self.master = master
        master.title("Countdown Timer")

        self.remaining_time = timedelta(minutes=5)  # Initial countdown time
        self.var = tk.StringVar()

        self.label = tk.Label(master, textvariable=self.var, font=("Helvetica", 24))
        self.label.pack(pady=20)

        self.start_button = tk.Button(master, text="Start Countdown", command=self.start_countdown)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop Countdown", command=self.stop_countdown, state=tk.DISABLED)
        self.stop_button.pack()

        # self.update_display()
        # self.start_countdown()

    def update_display(self):
        self.var.set(str(self.remaining_time))
        if self.remaining_time > timedelta():
            self.remaining_time -= timedelta(seconds=1)
            self.master.after(1000, self.update_display)
        else:
            self.var.set("Countdown Complete")

    def start_countdown(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.update_display()

    def stop_countdown(self):
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.remaining_time = timedelta(minutes=5)
        self.var.set("Countdown Stopped")


root = tk.Tk()
app = CountdownApp(root)
root.mainloop()
