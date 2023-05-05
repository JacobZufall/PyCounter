from tkinter import Button
import _g


class IncrementalButton(Button):
    def increment_number(self):

        _g.count_number += self

        main.label.config(text=_g.count_number)

    def __init__(self, parent, *args, **kwargs):
        super().__init__(self, parent, *args, **kwargs)
        self.root = kwargs.get("root")

        amount = kwargs.get("amount")

        if amount > 0:
            self.text = f"+{amount}"
        elif amount < 0:
            self.text = f"-{amount}"
        else:
            self.text = f"?{amount}"

        self.command = self.increment_number(amount)
