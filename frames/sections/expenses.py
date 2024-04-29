
import tkinter as tk
import ttkbootstrap as tb

import uuid

from components.card import Card
from datastructures.stack import Stack


categories = ["Food", "Transportation", "Clothing", "Saving"]

class Expenses(tb.Frame):
    def __init__(self, app_state, master=None):
        super().__init__(master, borderwidth=0)
        self.heading = tb.Frame(self)
        self.headingText = tb.Label(self.heading, text="Expenses", font=("Helvetica", 12))
        self.headingText.pack(expand=True, fill='x', padx=10, side="left")
        self.heading.pack(fill='x', padx=10)


        # initilize data
        self.expenses_array = []
        self.action_history = Stack()
        self.saving_milestones = app_state.get_data('saving_milestones')

        # expense name
        self.label = tb.Label(self, text="Name", font=("Helvetica", 10))
        self.label.pack()
        self.nameInput = tb.Entry(self)
        self.nameInput.pack(side="top", fill="x", pady=3, padx=20)

        # expense amount
        self.label = tb.Label(self, text="Amount", font=("Helvetica", 10))
        self.label.pack()
        self.amountInput = tb.Entry(self)
        self.amountInput.pack(side="top", fill="x", pady=3, padx=20)

        # expense category
        self.label = tb.Label(self, text="Category", font=("Helvetica", 10))
        self.label.pack()
        self.category = tb.Combobox(self, values=categories)
        self.category.pack(side="top", fill="x", pady=3, padx=20)
        self.category.current(0)

        # Add button
        self.add = tb.Button(self, bootstyle = 'success outline', text='Add', command=self.addExpense)
        self.add.pack(pady=10, fill="x", padx=20)

        # Scrollable Cards
        # self.expenseCards = tb.Frame(self)
        # self.headingText = tb.Label(self.heading, text="Expenses", font=("Helvetica", 12))
        # self.headingText.pack(expand=True, fill='x', padx=10, side="left")
        # self.expenseCards.pack(fill='x', padx=10)

        # State management
        self.app_state = app_state
        self.app_state.register_observer(self)
        self.app_state.set_data('name', 'naol fekadu')

        print(f"App state was updated {self.app_state['name']}")

        self.renderCards()


        # Undo button
        self.undo = tb.Button(self, bootstyle = 'warning outline', text='Undo', command=self.undo)
        self.undo.pack(pady=10, fill="x", padx=20)

    def clickMe(self):
        print(f"Expenses")
        self.app_state.set_data('name', 'naol fekadu')
    
    def renderCards(self):
        my_frame = tb.Frame(self)
        my_frame.pack(pady=5, fill="both", expand=True)

        # Create a canvas to contain the cards
        canvas = tb.Canvas(my_frame)
        canvas.pack(side="left", fill="both", expand=True)

        scrollPane = tb.Scrollbar(my_frame, orient='vertical', command=canvas.yview)
        scrollPane.pack(side="right", fill="y")

        # Attach the canvas to the scrollbar
        canvas.configure(yscrollcommand=scrollPane.set)

        # Update the weight of the columns to give more space to the canvas
        my_frame.grid_columnconfigure(0, weight=1)
        my_frame.grid_columnconfigure(1, weight=0)

        if self.expenses_array:
            for expense in self.expenses_array:
                card = Card(canvas, name=expense['name'], amount=expense['amount'])
                canvas.create_window((0, 0), window=card, anchor="nw")

        


    def addExpense(self):
        # print(f"I am adding an expense {self.nameInput.get()} {self.amountInput.get()} {self.category.get()} ")
        # add expenses to expenses array
        expense_id = uuid.uuid4()
        print(f"The amout input is: 👉 {self.amountInput.get()}")
        new_expense = {
            'id': expense_id,
            'name': self.nameInput.get(),
            'amount': 500,
            'category': self.category.get()
        }
        self.expenses_array.append(new_expense)
        print(self.expenses_array)

        # update state
        self.app_state.set_data('expenses_array', self.expenses_array)

        # add to stack for undo operation
        self.action_history.push({
            'action': 'add_expense',
            'expense_id': expense_id
        })

        if new_expense['category'] == 'Saving' and self.getTotalSaving() >= self.saving_milestones.peek():
            removed_milestone = self.saving_milestones.dequeue()
            # add to stack for undo operation
            self.action_history.push({
                'action': 'remove_milestone',
                'milestone': removed_milestone
            })
            
    def undo(self):
        print(f"I am undoing {self.action_history.peek()}")
        undo_action = self.action_history.pop()
        if undo_action['action'] == 'add_expense':
            for index, value in enumerate(self.expenses_array):
                if value['id'] == undo_action['expense_id']:
                    del self.expenses_array[index]
        elif undo_action['action'] == 'remove_milestone':
            self.saving_milestones.enqueue({ 'amount': undo_action['amount']})
        print(f"Array now {self.expenses_array}")

        # update state
        self.app_state.set_data('expenses_array', self.expenses_array)
    
    def getTotalSaving(self):
        total_saving = 0
        for x in self.expenses_array:
            if x['category'] == 'Saving':
                total_saving += x['amount']
        return total_saving
    
    def update(self):
        print(f"Update function: {self.app_state['name']}")
        # update saving_milestones state
        self.saving_milestones = self.app_state.get_data('saving_milestones')
        self.renderCards()
        pass





        # super().__init__(master)
        # self.label = tk.Label(self, text="Header", font=("Helvetica", 16))
        # self.label.pack(pady=10)
