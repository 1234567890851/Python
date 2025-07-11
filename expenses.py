import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
from datetime import date

FILENAME = "expenses.csv"

# Save header if file doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Note", "Date"])

# Save new expense
def save_expense():
    try:
        amount = float(entry_amount.get())
        category = entry_category.get()
        note = entry_note.get()
        today = date.today().isoformat()

        if category.strip() == "":
            messagebox.showerror("Error", "Category is required")
            return

        with open(FILENAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([amount, category, note, today])

        messagebox.showinfo("Saved", "Expense recorded!")
        entry_amount.delete(0, tk.END)
        entry_category.delete(0, tk.END)
        entry_note.delete(0, tk.END)
        load_expenses()

    except ValueError:
        messagebox.showerror("Error", "Amount must be a number")

# Load and display expenses
def load_expenses():
    tree.delete(*tree.get_children())
    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            tree.insert("", tk.END, values=(row["Amount"], row["Category"], row["Note"], row["Date"]))
            total += float(row["Amount"])
    label_total.config(text=f"Total Spent: ₹{total:.2f}")

# GUI setup
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("2000x1900")

# Input section
tk.Label(root, text="Amount (₹):").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

tk.Label(root, text="Category:").pack()
entry_category = tk.Entry(root)
entry_category.pack()

tk.Label(root, text="Note (optional):").pack()
entry_note = tk.Entry(root)
entry_note.pack()

tk.Button(root, text="Add Expense", command=save_expense).pack(pady=10)

# Table view using Treeview
columns = ("Amount", "Category", "Note", "Date")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
tree.pack(expand=True, fill="both", pady=10)

# Scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Total label
label_total = tk.Label(root, text="Total Spent: ₹0.00", font=("Arial", 12, "bold"))
label_total.pack(pady=5)

load_expenses()

root.mainloop()
