import tkinter as tk
from datetime import datetime

def update_clock():
    clock_label.config(text=datetime.now().strftime("%I:%M:%S %p"))
    root.after(1000, update_clock)

root = tk.Tk()
root.title("Clock")
root.geometry("320x150")
root.resizable(False, False)

clock_label = tk.Label(root, font=("Arial", 32, "bold"))
clock_label.pack(pady=(20, 5))

experience_label = tk.Label(
    root,
    text="Experience: 3 yrs",
    font=("Arial", 16)
)
experience_label.pack()

update_clock()
root.mainloop()