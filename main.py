import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()

root.title("PyCounter")
root.geometry("600x500")
root.iconbitmap("assets/icon.ico")
root.resizable(False, False)

count_number: int = 0

label = tk.Label(root, text=count_number)
label.grid(row=0, rowspan=2, column=0, columnspan=3, sticky="NESW")


def increment_number(amount: int):
    global label
    global count_number

    count_number += amount

    label.config(text=count_number)


def reset_number():
    global label
    global count_number

    count_number = 0
    label.config(text=0)


reset = ttk.Button(root, text="Reset", command=reset_number)
reset.grid(row=2, column=0, columnspan=3, sticky="NESW")

plus_one = ttk.Button(root, text="+1", command=lambda: increment_number(1))
minus_one = ttk.Button(root, text="-1", command=lambda: increment_number(-1))
plus_one.grid(row=0, column=3, sticky="NESW")
minus_one.grid(row=0, column=4, sticky="NESW")

plus_ten = ttk.Button(root, text="+10", command=lambda: increment_number(10))
minus_ten = ttk.Button(root, text="-10", command=lambda: increment_number(-10))
plus_ten.grid(row=1, column=3, sticky="NESW")
minus_ten.grid(row=1, column=4, sticky="NESW")

plus_hundred = ttk.Button(root, text="+100", command=lambda: increment_number(100))
minus_hundred = ttk.Button(root, text="-100", command=lambda: increment_number(-100))
plus_hundred.grid(row=2, column=3, sticky="NESW")
minus_hundred.grid(row=2, column=4, sticky="NESW")

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    if i < 3:
        root.grid_rowconfigure(i, weight=1)

root.mainloop()
