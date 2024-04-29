# main.py
import tkinter as tk
import ttkbootstrap as tb
# from frames.sections.expenses import Expenses
# from frames.sections.savings import savings
# from frames.sections.viz import viz

from frames.header import Header
from frames.body import Body


class MyApp(tb.Window):
    def __init__(self):
        super().__init__(themename="superhero")
        # Configs
        self.title("Budget Tracker")
        self.geometry('1000x600')
        self.resizable(False, False)

        # Header app name
        self.header = Header(self)
        self.header.pack(side="top", fill="x", padx=20)

        # Main Content
        self.body = Body(self)
        self.body.pack(side="top", expand=True, fill="both", padx=20)
        
if __name__ == "__main__":
    app = MyApp()
    app.mainloop()
