import tkinter as tk
from tkinter import messagebox

def calculate_budget():
    try:
        budget = float(budget_entry.get())
        spending = float(spending_entry.get())
        remaining = budget - spending
        if remaining > 0:
            messagebox.showinfo("Result", f"You are within budget. Remaining amount: ${remaining:.2f}")
        else:
            messagebox.showwarning("Result", f"You have exceeded the budget by ${-remaining:.2f}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers for budget and spending.")

# Create the main window
root = tk.Tk()
root.title("Budget Manager")

# Create and place the budget label and entry
budget_label = tk.Label(root, text="Enter your budget:")
budget_label.pack()
budget_entry = tk.Entry(root)
budget_entry.pack()

# Create and place the spending label and entry
spending_label = tk.Label(root, text="Enter your spending:")
spending_label.pack()
spending_entry = tk.Entry(root)
spending_entry.pack()

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_budget)
calculate_button.pack()

# Run the application
root.mainloop()