import tkinter


class ResetButton(tkinter.Button):
    @staticmethod
    def reset_number():
        global label
        global count_number

        count_number = 0
        label.config(text=0)

    def __init__(self, root, amount, row, column, sticky):
        super().__init__(self, root, amount, row, column, sticky)
