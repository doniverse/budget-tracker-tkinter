import tkinter as tk
import ttkbootstrap as tb

class Header(tb.Frame):
    def __init__(self, master=None):
        super().__init__(master, borderwidth=0)
        self.label = tb.Label(self, text="Budget Tracker", font=("Helvetica", 19))
        self.label.pack(pady=12, side="left")
    def clickMe(self):
        print("I am in Header")



        # super().__init__(master)
        # self.label = tk.Label(self, text="Header", font=("Helvetica", 16))
        # self.label.pack(pady=10)
