import tkinter as tk
import ttkbootstrap as tb

class Savings(tb.Frame):
    def __init__(self, app_state, master=None):
        super().__init__(master, borderwidth=0)

        self.heading = tb.Frame(self)
        self.headingText = tb.Label(self.heading, text="Savings Milestone", font=("Helvetica", 12))
        self.headingText.pack(expand=True, fill='x', padx=10, side="left")
        self.heading.pack(fill='x', padx=10)

        # App state
        self.app_state = app_state
        self.app_state.register_observer(self)
        print(f"App state was updated {self.app_state['name']} savings")


        # Initializing data
        self.saving_milestones = app_state.get_data('saving_milestones')

        # milestone amount
        self.label = tb.Label(self, text="Name", font=("Helvetica", 10))
        self.label.pack()
        self.milestoneInput = tb.Entry(self)
        self.milestoneInput.pack(side="top", fill="x", pady=3, padx=20)

        # Add button
        self.add = tb.Button(self, bootstyle = 'success outline', text='Set milestone', command=self.addMilestone)
        self.add.pack(pady=10, fill="x", padx=20)

    def clickMe(self):
        print(f"Savings")
        self.app_state.set_data('name', 'savings name')

    def addMilestone(self):
        self.saving_milestones.enqueue({ 'amount': int(self.milestoneInput.get())})
        print(f"Hello: {self.saving_milestones.peek()}")
    
    def update(self):
        print(f"Update function: {self.app_state['name']}")
        # Update component based on changes in the application state
        self.saving_milestones = self.app_state.get_data('saving_milestones')
        pass