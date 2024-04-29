import tkinter as tk
import ttkbootstrap as tb

class Card(tb.Frame):
    def __init__(self, master=None, name="", amount="", **kwargs):
        super().__init__(master, borderwidth=1, relief="solid", **kwargs)
        
        # Name label
        self.title_label = tb.Label(self, text=name, font=("Helvetica", 8, "bold"))
        self.title_label.pack(side='left', pady=(10, 10), padx=25)

        # Amount label
        self.description_label = tb.Label(self, text=amount, font=("Helvetica", 8, "bold"), wraplength=200)
        self.description_label.pack(side='left', pady=(10, 10))

        # Action button
        self.action_button = tb.Button(self, text="Del")
        self.action_button.pack(side='right', padx=10)

        
