import tkinter as tk
import ttkbootstrap as tb

from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  
NavigationToolbar2Tk)

from datastructures.AppState import AppState 

class Viz(tb.Frame):
    def __init__(self, app_state, master=None):
        super().__init__(master, borderwidth=0)

        self.heading = tb.Frame(self)
        self.headingText = tb.Label(self.heading, text="Visualizations", font=("Helvetica", 12))
        self.headingText.pack(expand=True, fill='x', padx=10, side="left")
        self.heading.pack(fill='x', padx=10)

        # App state
        self.app_state = app_state
        self.expenses_array = app_state.get_data('expenses_array')
        self.app_state.register_observer(self)
        self.app_state.set_data('name', 'cinna')
        print(f"App state was updated {self.app_state['name']} viz")

        # Create a Figure instance
        self.fig = Figure(figsize=(3.5, 3.5), dpi=100)
        self.renderGraph()

    def renderGraph(self):
        # Create data for the pie chart
        labels = [''] * 4
        sizes = [0] * len(labels)
        total_expense = 0

        for x in self.expenses_array:
            total_expense += x['amount']

        for x in self.expenses_array:
            if x['category'] == 'Saving':
                labels[3] = 'Saving'
                sizes[3] += (x['amount'] / total_expense) * 100 
            elif x['category'] == 'Food':
                labels[0] = 'Food'
                sizes[0] += (x['amount'] / total_expense) * 100 
            elif x['category'] == 'Transportation':
                labels[1] = 'Transportation'
                sizes[1] += (x['amount'] / total_expense) * 100 
            elif x['category'] == 'Clothing':
                labels[2] = 'Clothing'
                sizes[2] += (x['amount'] / total_expense) * 100 
        
        if len(self.expenses_array) > 0:
            if hasattr(self, 'ax'):
                self.canvas.get_tk_widget().pack_forget()
                self.ax.clear()
            self.ax = self.fig.add_subplot(111)
            self.ax.axis('off')
            print(f"Plotting graph 👉: {total_expense} - {sizes} - {self.expenses_array}")

            # Plot the pie chart
            self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
            

            # Create a canvas
            self.canvas = FigureCanvasTkAgg(self.fig, master=self)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()



        
    def clickMe(self):
        print(f"Viz")
        self.app_state.set_data('name', 'milko')

    def update(self):
        print(f"🌏 the data of expenses has changed to: {self.app_state['expenses_array']}")
        print(f"🌏 the data of expenses has changed to: {self.expenses_array}")
        self.expenses_array = self.app_state.get_data('expenses_array')
        self.renderGraph()
        print(f"Update function: {self.app_state['name']}")
        # Update component based on changes in the application state
        pass
