import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import os

root = tk.Tk()

root.geometry("750x450")
root.title("Expense Tracker")
root.configure(background="#232323")

item_list = []
csv_file = "expense_tracker.csv"  # Name of the CSV file

# Function to add an item
def add_item():
    item = item_txt.get()
    qty = qty_txt.get()
    cost = cost_txt.get()
    total = int(qty) * int(cost)
    
    single_item_lbl = tk.Label(
        frame2, text=f"{item}\t\t{qty}\t\t{cost}\t\t{total}",
        bg="#232323", fg="#ffffff", font=("Arial", 15), anchor="w"
    )
    
    single_item = {"Item": item, "Quantity": qty, "Cost": cost, "Total Amount": total}
    item_list.append(single_item)
    save_to_csv()  # Save the latest item to the CSV file
    single_item_lbl.pack(pady=5)

# Function to clear input fields
def clear_item():
    item_txt.delete(0, "end")
    qty_txt.delete(0, "end")
    cost_txt.delete(0, "end")

# Function to save the latest item to the CSV file
def save_to_csv():
    # Convert the latest dictionary in the list to a DataFrame
    df = pd.DataFrame([item_list[-1]])  # Only the last item
    # Check if the file exists
    if os.path.exists(csv_file):
        # Append the single item to the existing CSV
        df.to_csv(csv_file, mode='a', header=False, index=False)
    else:
        # Create a new CSV file with headers
        df.to_csv(csv_file, mode='w', header=True, index=False)

# Function to analyze expenses
def analyze():
    if os.path.exists(csv_file):
        df = pd.read_csv(csv_file)
        items = df['Item']
        total = df['Total Amount']
        fig = plt.figure(figsize=(10, 5))
        plt.bar(items, total, color='red', width=0.4)
        plt.title("Expense Tracker Analyzer")
        plt.ylabel("Cost of the items")
        plt.xlabel("Item purchased")
        plt.show()
    else:
        print("No data to analyze. Please add items first.")

# Title Label
title_lbl = tk.Label(root, text="Expense Tracker", bg="#232323", fg="#ffffff", font=("Arial", 20))
title_lbl.pack(pady=30)

# Item Label and Entry
item_lbl = tk.Label(root, text="Item", bg="#232323", fg="#ffffff", font=("Arial", 15))
item_lbl.pack(pady=(30, 5))
item_txt = tk.Entry(root, font=("Arial", 15))
item_txt.pack()

# Quantity Label and Entry
qty_lbl = tk.Label(root, text="Quantity", bg="#232323", fg="#ffffff", font=("Arial", 15))
qty_lbl.pack(pady=(30, 5))
qty_txt = tk.Entry(root, font=("Arial", 15))
qty_txt.pack()

# Cost Label and Entry
cost_lbl = tk.Label(root, text="Cost", bg="#232323", fg="#ffffff", font=("Arial", 15))
cost_lbl.pack(pady=(30, 5))
cost_txt = tk.Entry(root, font=("Arial", 15))
cost_txt.pack()

# Buttons
frame1 = tk.Frame(root, bg="#232323")
add_btn = tk.Button(frame1, text="Add Item", bg="#2a2a2a", fg="#ffffff", font=("Arial", 15), command=add_item)
add_btn.pack(padx=10, pady=20, side=tk.LEFT)

clear_btn = tk.Button(frame1, text="Clear", bg="#2a2a2a", fg="#ffffff", font=("Arial", 15), command=clear_item)
clear_btn.pack(padx=10, pady=20, side=tk.RIGHT)
frame1.pack()

# Expenses Section
display_lbl = tk.Label(root, text="Expenses", bg="#232323", fg="#ffffff", font=("Arial", 15))
display_lbl.pack(pady=(30, 5))

frame2 = tk.Frame(root, bg="#232323")
head_lbl = tk.Label(frame2, text="Item\t\tQuantity\t\tUnit Cost\t\tTotal", bg="#232323", fg="#ffffff", font=("Arial", 15))
head_lbl.pack(pady=5)
frame2.pack() 

# Analyze Button
analyze_btn = tk.Button(root, text="Analyze", bg="#2a2a2a", fg="#ffffff", font=("Arial", 15), command=analyze)
analyze_btn.pack(pady=20)

root.mainloop()
