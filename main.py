import tkinter as tk
from incremental_button import IncrementalButton as ic_button
import _g


global label


class Main(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(self, *args, **kwargs)
        self.pack(side="top", fill="both", expand=True)

        label = tk.Label(root, text=_g.count_number)

        plus_one = ic_button(root, amount=1)


if __name__ == "__main__":
    # Nothing inside this conditional needs to be changed.
    root = tk.Tk()
    root.title("PyCounter")
    root.geometry("600x500")  # Default window size.
    root.iconbitmap("assets/icon.ico")  # Application icon.
    root.resizable(False, False)
    Main(root)
    root.mainloop()
