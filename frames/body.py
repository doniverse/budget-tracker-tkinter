import tkinter as tk
import ttkbootstrap as tb

# from sections.expenses import Expenses
from datastructures.AppState import AppState
from frames.sections.expenses import Expenses
from frames.sections.savings import Savings
from frames.sections.viz import Viz

# DS
from datastructures.queue import Queue
from datastructures.AppState import AppState

        
class Body(tb.Frame):
    def __init__(self, master=None):
        super().__init__(master, borderwidth=0)
        # self.label = tb.Label(self, text="Body", font=("Helvetica", 16), background='red')
        # self.label.pack(pady=10, side="left")

        # App state
        self.app_state = AppState()
        self.app_state.set_data('expenses_array', [])
        self.app_state.set_data('saving_milestones', Queue())
        
        self.expenses = Expenses(self.app_state)
        self.expenses.pack(side="left", fill="both", expand=True)
        self.expenses.clickMe()

        self.visualization = Viz(self.app_state)
        self.visualization.pack(side="left", fill="both", expand=True)
        self.visualization.clickMe()

        self.savings = Savings(self.app_state)
        self.savings.pack(side="left", fill="both", expand=True)
        self.savings.clickMe()

    def clickMe(self):
        print("I am in Body")

 
# Create custom button component
# self.custom_button = CustomButton(self)
# self.custom_button.pack(pady=10)
# self.expenses = Expenses()
