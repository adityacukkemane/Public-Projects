import tkinter as tk
from tkinter import messagebox

def calculate_budget():
    try:
        budget = float(budget_entry.get())
        spending = float(spending_entry.get())
        if budget < 0 or spending < 0:
            raise ValueError("Negative numbers are not allowed.")
        remaining = budget - spending
        if remaining > 0:
            messagebox.showinfo("Result", f"You are within budget. Remaining amount: ${remaining:.2f}")
        else:
            messagebox.showwarning("Result", f"You have exceeded the budget by ${-remaining:.2f}")
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except TypeError:
        messagebox.showerror("Error", "Please enter valid numbers for budget and spending.")

# Create the main window
root = tk.Tk()
root.title("Budget Manager")
root.attributes('-fullscreen', True)

# Define a larger font
large_font = ("Helvetica", 16)

# Create and place the budget label and entry
budget_label = tk.Label(root, text="Enter your budget:", font=large_font)
budget_label.pack(pady=10)
budget_entry = tk.Entry(root, font=large_font)
budget_entry.pack(pady=10)

# Create and place the spending label and entry
spending_label = tk.Label(root, text="Enter your spending:", font=large_font)
spending_label.pack(pady=10)
spending_entry = tk.Entry(root, font=large_font)
spending_entry.pack(pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_budget, font=large_font)
calculate_button.pack(pady=10)

# Create and place the exit button
exit_button = tk.Button(root, text="Exit the App", command=root.quit, font=large_font, bg="red", fg="white")
exit_button.pack(pady=10)

# Run the application
root.mainloop()